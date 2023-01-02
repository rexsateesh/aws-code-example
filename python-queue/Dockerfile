FROM --platform=linux/amd64 public.ecr.aws/docker/library/python:3

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
RUN which aws
RUN aws --version
RUN aws configure set region us-east-1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python main.py
