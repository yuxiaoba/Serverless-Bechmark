# Use the lightweight Python image which pre-installed the dependency
FROM harbor.test.com/knative/python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

CMD python app.py
