from py2neo import Graph
import json
graph = Graph(username='neo4j', password='123456')
internjson = json.load(open("data/details.json","r"))
query = """CREATE(internships:Internships{name:"InternshipDetails"})
           WITH {internjson} as data,internships as i
           FOREACH(n in data|CREATE UNIQUE(details:Details{internship:n.internship,organisation:n.organisation,stipend:n.stipend,start_date:n.start_date,duration:n.duration,posted_on:n.posted_on,last_date_to_apply:n.last_date_to_apply})-[:located_in]->(location:Location{name:n.location})<-[:in]-(i))
"""
graph.run(query,internjson=internjson)
