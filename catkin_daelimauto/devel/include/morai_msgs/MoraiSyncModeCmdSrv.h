// Generated by gencpp from file morai_msgs/MoraiSyncModeCmdSrv.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_MORAISYNCMODECMDSRV_H
#define MORAI_MSGS_MESSAGE_MORAISYNCMODECMDSRV_H

#include <ros/service_traits.h>


#include <morai_msgs/MoraiSyncModeCmdSrvRequest.h>
#include <morai_msgs/MoraiSyncModeCmdSrvResponse.h>


namespace morai_msgs
{

struct MoraiSyncModeCmdSrv
{

typedef MoraiSyncModeCmdSrvRequest Request;
typedef MoraiSyncModeCmdSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoraiSyncModeCmdSrv
} // namespace morai_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrv > {
  static const char* value()
  {
    return "df0fcb0eae8a1f37d527d8331f8eb734";
  }

  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrv&) { return value(); }
};

template<>
struct DataType< ::morai_msgs::MoraiSyncModeCmdSrv > {
  static const char* value()
  {
    return "morai_msgs/MoraiSyncModeCmdSrv";
  }

  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrv&) { return value(); }
};


// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrvRequest> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiSyncModeCmdSrvRequest> should match
// service_traits::DataType< ::morai_msgs::MoraiSyncModeCmdSrv >
template<>
struct DataType< ::morai_msgs::MoraiSyncModeCmdSrvRequest>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiSyncModeCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrvResponse> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiSyncModeCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiSyncModeCmdSrvResponse> should match
// service_traits::DataType< ::morai_msgs::MoraiSyncModeCmdSrv >
template<>
struct DataType< ::morai_msgs::MoraiSyncModeCmdSrvResponse>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiSyncModeCmdSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeCmdSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_MORAISYNCMODECMDSRV_H
