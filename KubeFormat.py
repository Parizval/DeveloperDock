strategy = {}

NormalHeading = {"Kubeless":" Kubeless Functions" , 
    "Round Robin":"Round Robin Load Balancer (v2)","Ring Hash":"Ring Hash Load Balancing Algorithm"}

NormalDocs =  {"Kubeless":"<a href='https://kubeless.io'  target='_blank'>Kubeless Solution</a>" ,
    "Round Robin":"<a href='https://envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/load_balancers.html' target='_blank'>Round Robing using kube-proxy or Envoy Proxy</a>",
    "Ring Hash":"<a href='https://envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/load_balancers.html' target='_blank'> Ring Hash using Envoy Proxy</a>"}

def Formatting(result):
    data = {}
    data['Heading'] = NormalHeading[result]
    data['Link'] = NormalDocs[result]

    return data 