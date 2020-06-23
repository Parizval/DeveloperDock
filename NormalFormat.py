strategy = {}

NormalHeading = {"Network":"Network Load Balancer (v2)" , "Serverless":"AWS Lambda",
    "Application":"Application Load Balancer (v2)","Sticky":"Session Based Load Balancer"}

NormalDocs =  {"Network":"<a href='https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html'  target='_blank'>Link to AWS Docs</a>" ,
 "Serverless":"<a href='https://docs.aws.amazon.com/lambda/index.html' target='_blank'>Link to AWS Docs</a>",
    "Application":"<a href='https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html' target='_blank'>Link to AWS Docs</a>",
    "Sticky":"<a href='https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html' target='_blank'>Link to AWS Docs</a>"}

def Formatting(result):
    data = {}
    data['Heading'] = NormalHeading[result]
    data['Link'] = NormalDocs[result]

    return data 