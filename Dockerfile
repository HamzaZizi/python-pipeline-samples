# FROM python:3.10.6-alpine
# WORKDIR /python-pipeline-samples
# ADD . /python-pipeline-samples
# RUN pip install -r requirements.txt
# CMD ["python3", "./app.py"]


# FROM python:3.10.6-alpine
# ENV APPD_AGENT_VERSION=24.11.0.7213

# WORKDIR /python-pipeline-samples
# ADD . /python-pipeline-samples
# RUN pip install -U appdynamics==${APPD_AGENT_VERSION} -r requirements.txt
# CMD pyagent run --use-manual-proxy python3 ./app.py



FROM python:3.7

# Use latest version from https://pypi.org/project/appdynamics/#history
ENV APPD_AGENT_VERSION=21.12.2.4693

# Set working directory inside the container
WORKDIR /app

# Copy the necessary files from your local directory into the container
COPY app.py /app/
COPY requirements.txt /app/
COPY appd-python-config.yaml /app/
COPY .harness/ /app/.harness/
COPY templates/ /app/templates/
COPY docs/ /app/docs/
RUN chmod +x ./app.py

EXPOSE 8080

RUN pip install -U appdynamics==${APPD_AGENT_VERSION} -r requirements.txt

CMD pyagent run --use-manual-proxy python ./app.py

