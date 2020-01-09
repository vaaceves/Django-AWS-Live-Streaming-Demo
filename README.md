# Django-AWS-Live-Streaming-Demo 

This is a personal repository to practice uploading videos and converting them into live streaming with React, Django and AWS.

Steps:
1. Split video into chunks with React.
2. Request Django API to upload and merge video chunks and store them in [Amazon S3](https://aws.amazon.com/s3/).
3. Use [AWS Lambda](https://aws.amazon.com/lambda/) and [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) to convert videos into [HLS (HTTP Live Streaming)](https://en.wikipedia.org/wiki/HTTP_Live_Streaming). 
4. Create a live streadming player with React to play the S3 HLS.

## Official Simple Serverless Video On Demand (VOD) Workflow
![Official Workflow](https://d2908q01vomqb2.cloudfront.net/5b384ce32d8cdef02bc3a139d4cac0a22bb029e8/2018/09/08/arch-3-1.jpg)


## TODO:
Django
React
Lambda

## Resource
- [React - hls](https://github.com/mingxinstar/react-hls#readme)
- [Lambda - aws-media-services-simple-vod-workflow](https://github.com/aws-samples/aws-media-services-simple-vod-workflow)
