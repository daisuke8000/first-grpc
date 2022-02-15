import grpc
import pancake_pb2_grpc
import pancake_pb2


def baker():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pancake_pb2_grpc.PancakeBakerServiceStub(channel)
        response = stub.Bake(pancake_pb2.BakeRequest(menu=2))
        return response


def report():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pancake_pb2_grpc.PancakeBakerServiceStub(channel)
        response = stub.Report(pancake_pb2.ReportRequest())
        return response


if __name__ == "__main__":
    print(baker())
    print(report())
