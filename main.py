from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url="http://127.0.0.1:9945"
)

print(substrate.rpc_request("rpc_methods", []))
