require 'date'
require "httparty"
require 'json'
require 'logger'
require 'optimist'

$stdout.sync = true
@logger = Logger.new(STDOUT)
@logger.level = Logger::DEBUG

# Poll the USGS feed for real-time earthquake readings
def pull_hourly_earthquake(lastTime, sink)
    # Get all detected earthquakes in the last hour
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/" \
    + "summary/all_hour.geojson"
    response = HTTParty.get(url)
    j = JSON.parse(response.body)

    # Keep track of latest recorded event, reporting all
    # if none have been tracked so far
    cycleLastTime = lastTime

    # Parse each reading and emit new ones as events
    j["features"].each do |f|
        time = f["properties"]["time"]

        if time > lastTime
            msg = {
                time: DateTime.strptime(time.to_s,'%Q'),
                id: f["id"],
                type: "quake",
                measure: f["properties"]["mag"],
                lat: f["geometry"]["coordinates"][1],
                long: f["geometry"]["coordinates"][0]
            }

            publish_event(msg, sink)
        end

        # Keep track of latest reading
        if time > cycleLastTime
            cycleLastTime = time
        end
    end

    lastTime = cycleLastTime
    return lastTime
end

# POST event to provided sink
def publish_event(message, sink)
    @logger.info("Sending #{message[:id]} to #{sink}")
    puts message.to_json
    r = HTTParty.post(sink, 
        :headers => {
            'Content-Type' => 'text/plain',
            'ce-specversion' => '0.2',
            'ce-type' => 'dev.knative.naturalevent.quake',
            'ce-source' => 'dev.knative.usgs'
        }, 
        :body => message.to_json)
    
    if r.code != 200
        @logger.error("Error! #{r}")
    end
end


# Parse CLI flags
opts = Optimist::options do
    banner <<-EOS
Poll USGS Real-Time Earthquake data

Usage:
  ruby usgs-event-source.rb

EOS
    opt :interval, "Poll Frequenvy", 
        :default => 10
    opt :sink, "Sink to send events", 
        :default => "http://localhost:8080"
end

# Begin polling USGS data
lastTime = 0
@logger.info("Polling every #{opts[:interval]} seconds")
while true do 
    @logger.debug("Polling . . .")
    lastTime = pull_hourly_earthquake(lastTime, opts[:sink])
    sleep(opts[:interval])
end