import json

from colony_toolbelt.tools.kafka import Kafka

kafka = Kafka(bootstrap_servers="kafka-headless.kafka:29092",
              producer_kwargs=dict(
                  value_serializer=lambda v: v and json.dumps(v).encode("utf-8")
                )
              )


