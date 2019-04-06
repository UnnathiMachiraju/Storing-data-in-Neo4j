from py2neo import Graph

graph = Graph(username='neo4j', password='123456')

#looking for interns in Delhi, return all the children of node Delhi
query1="""MATCH(n)-[:located_in]->(m:Location{name:"Delhi"}) RETURN n"""

#finding locations where there is an Operations internship
query2="""MATCH(n)-[:located_in]->(m) WHERE n.internship="Operations" RETURN m.name"""

#Returns the organisations in which operations intern is available
query3="""MATCH(n) WHERE n.internship="Operations" RETURN n.organisation """

print(graph.run(query1).data())
print(graph.run(query2).data())
print(graph.run(query3).data())
