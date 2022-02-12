## gRPC Server and Client call

### server run
```bash
cd api && go run sever/server.go
```

### client call
```bash
grpc_cli call localhost:50051 pancake.maker.PancakeBakerService.Bake 'menu: 1'
```