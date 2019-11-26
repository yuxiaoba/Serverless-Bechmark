# usgs-event-source

A custom [Knative event source](https://github.com/knative/docs/tree/master/eventing) built as a ContainerSource. Periodically polls the [USGS Event Feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson) and emits events to the provided sink.
