from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "toadface")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

    # Get the name of all 42 year-olds
    records, summary, keys = driver.execute_query(
        "MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties.title",
        database_="neo4j",
    )

    # Loop through results and do something with them
    for person in records:
        print(person)

    # Summary information
    print("The query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records),
        time=summary.result_available_after,
    ))