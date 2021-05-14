// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: hello.proto
#ifndef GRPC_hello_2eproto__INCLUDED
#define GRPC_hello_2eproto__INCLUDED

#include "hello.pb.h"

#include <grpc++/impl/codegen/async_stream.h>
#include <grpc++/impl/codegen/async_unary_call.h>
#include <grpc++/impl/codegen/method_handler_impl.h>
#include <grpc++/impl/codegen/proto_utils.h>
#include <grpc++/impl/codegen/rpc_method.h>
#include <grpc++/impl/codegen/service_type.h>
#include <grpc++/impl/codegen/status.h>
#include <grpc++/impl/codegen/stub_options.h>
#include <grpc++/impl/codegen/sync_stream.h>

namespace grpc {
class CompletionQueue;
class Channel;
class RpcService;
class ServerCompletionQueue;
class ServerContext;
}  // namespace grpc

namespace hello {

class HelloService final {
 public:
  class StubInterface {
   public:
    virtual ~StubInterface() {}
    // This thing just says Hello to anyone
    // SayHello('Euler') -> Hello, Euler!
    virtual ::grpc::Status SayHello(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::hello::HelloResp* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>> AsyncSayHello(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>>(AsyncSayHelloRaw(context, request, cq));
    }
    // Strict Version responds only to requests which have `Name` length
    // less than 10 characters
    virtual ::grpc::Status SayHelloStrict(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::hello::HelloResp* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>> AsyncSayHelloStrict(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>>(AsyncSayHelloStrictRaw(context, request, cq));
    }
  private:
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>* AsyncSayHelloRaw(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::hello::HelloResp>* AsyncSayHelloStrictRaw(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) = 0;
  };
  class Stub final : public StubInterface {
   public:
    Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel);
    ::grpc::Status SayHello(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::hello::HelloResp* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>> AsyncSayHello(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>>(AsyncSayHelloRaw(context, request, cq));
    }
    ::grpc::Status SayHelloStrict(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::hello::HelloResp* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>> AsyncSayHelloStrict(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>>(AsyncSayHelloStrictRaw(context, request, cq));
    }

   private:
    std::shared_ptr< ::grpc::ChannelInterface> channel_;
    ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>* AsyncSayHelloRaw(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::hello::HelloResp>* AsyncSayHelloStrictRaw(::grpc::ClientContext* context, const ::hello::HelloReq& request, ::grpc::CompletionQueue* cq) override;
    const ::grpc::RpcMethod rpcmethod_SayHello_;
    const ::grpc::RpcMethod rpcmethod_SayHelloStrict_;
  };
  static std::unique_ptr<Stub> NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());

  class Service : public ::grpc::Service {
   public:
    Service();
    virtual ~Service();
    // This thing just says Hello to anyone
    // SayHello('Euler') -> Hello, Euler!
    virtual ::grpc::Status SayHello(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response);
    // Strict Version responds only to requests which have `Name` length
    // less than 10 characters
    virtual ::grpc::Status SayHelloStrict(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response);
  };
  template <class BaseClass>
  class WithAsyncMethod_SayHello : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithAsyncMethod_SayHello() {
      ::grpc::Service::MarkMethodAsync(0);
    }
    ~WithAsyncMethod_SayHello() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SayHello(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestSayHello(::grpc::ServerContext* context, ::hello::HelloReq* request, ::grpc::ServerAsyncResponseWriter< ::hello::HelloResp>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(0, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithAsyncMethod_SayHelloStrict : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithAsyncMethod_SayHelloStrict() {
      ::grpc::Service::MarkMethodAsync(1);
    }
    ~WithAsyncMethod_SayHelloStrict() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SayHelloStrict(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestSayHelloStrict(::grpc::ServerContext* context, ::hello::HelloReq* request, ::grpc::ServerAsyncResponseWriter< ::hello::HelloResp>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(1, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  typedef WithAsyncMethod_SayHello<WithAsyncMethod_SayHelloStrict<Service > > AsyncService;
  template <class BaseClass>
  class WithGenericMethod_SayHello : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithGenericMethod_SayHello() {
      ::grpc::Service::MarkMethodGeneric(0);
    }
    ~WithGenericMethod_SayHello() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SayHello(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithGenericMethod_SayHelloStrict : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithGenericMethod_SayHelloStrict() {
      ::grpc::Service::MarkMethodGeneric(1);
    }
    ~WithGenericMethod_SayHelloStrict() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status SayHelloStrict(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_SayHello : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithStreamedUnaryMethod_SayHello() {
      ::grpc::Service::MarkMethodStreamed(0,
        new ::grpc::StreamedUnaryHandler< ::hello::HelloReq, ::hello::HelloResp>(std::bind(&WithStreamedUnaryMethod_SayHello<BaseClass>::StreamedSayHello, this, std::placeholders::_1, std::placeholders::_2)));
    }
    ~WithStreamedUnaryMethod_SayHello() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status SayHello(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedSayHello(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::hello::HelloReq,::hello::HelloResp>* server_unary_streamer) = 0;
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_SayHelloStrict : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service *service) {}
   public:
    WithStreamedUnaryMethod_SayHelloStrict() {
      ::grpc::Service::MarkMethodStreamed(1,
        new ::grpc::StreamedUnaryHandler< ::hello::HelloReq, ::hello::HelloResp>(std::bind(&WithStreamedUnaryMethod_SayHelloStrict<BaseClass>::StreamedSayHelloStrict, this, std::placeholders::_1, std::placeholders::_2)));
    }
    ~WithStreamedUnaryMethod_SayHelloStrict() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status SayHelloStrict(::grpc::ServerContext* context, const ::hello::HelloReq* request, ::hello::HelloResp* response) final override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedSayHelloStrict(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::hello::HelloReq,::hello::HelloResp>* server_unary_streamer) = 0;
  };
  typedef WithStreamedUnaryMethod_SayHello<WithStreamedUnaryMethod_SayHelloStrict<Service > > StreamedUnaryService;
  typedef Service SplitStreamedService;
  typedef WithStreamedUnaryMethod_SayHello<WithStreamedUnaryMethod_SayHelloStrict<Service > > StreamedService;
};

}  // namespace hello


#endif  // GRPC_hello_2eproto__INCLUDED
