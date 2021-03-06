// Generated by gencpp from file morai_msgs/PREventSrv.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_PREVENTSRV_H
#define MORAI_MSGS_MESSAGE_PREVENTSRV_H

#include <ros/service_traits.h>


#include <morai_msgs/PREventSrvRequest.h>
#include <morai_msgs/PREventSrvResponse.h>


namespace morai_msgs
{

struct PREventSrv
{

typedef PREventSrvRequest Request;
typedef PREventSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct PREventSrv
} // namespace morai_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::morai_msgs::PREventSrv > {
  static const char* value()
  {
    return "a5cf1a2f9ad9d91c7dbbba6c3b888bda";
  }

  static const char* value(const ::morai_msgs::PREventSrv&) { return value(); }
};

template<>
struct DataType< ::morai_msgs::PREventSrv > {
  static const char* value()
  {
    return "morai_msgs/PREventSrv";
  }

  static const char* value(const ::morai_msgs::PREventSrv&) { return value(); }
};


// service_traits::MD5Sum< ::morai_msgs::PREventSrvRequest> should match
// service_traits::MD5Sum< ::morai_msgs::PREventSrv >
template<>
struct MD5Sum< ::morai_msgs::PREventSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::PREventSrv >::value();
  }
  static const char* value(const ::morai_msgs::PREventSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::PREventSrvRequest> should match
// service_traits::DataType< ::morai_msgs::PREventSrv >
template<>
struct DataType< ::morai_msgs::PREventSrvRequest>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::PREventSrv >::value();
  }
  static const char* value(const ::morai_msgs::PREventSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::morai_msgs::PREventSrvResponse> should match
// service_traits::MD5Sum< ::morai_msgs::PREventSrv >
template<>
struct MD5Sum< ::morai_msgs::PREventSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::PREventSrv >::value();
  }
  static const char* value(const ::morai_msgs::PREventSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::PREventSrvResponse> should match
// service_traits::DataType< ::morai_msgs::PREventSrv >
template<>
struct DataType< ::morai_msgs::PREventSrvResponse>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::PREventSrv >::value();
  }
  static const char* value(const ::morai_msgs::PREventSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_PREVENTSRV_H
