// Generated by gencpp from file morai_msgs/MoraiVehicleSpecSrv.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_MORAIVEHICLESPECSRV_H
#define MORAI_MSGS_MESSAGE_MORAIVEHICLESPECSRV_H

#include <ros/service_traits.h>


#include <morai_msgs/MoraiVehicleSpecSrvRequest.h>
#include <morai_msgs/MoraiVehicleSpecSrvResponse.h>


namespace morai_msgs
{

struct MoraiVehicleSpecSrv
{

typedef MoraiVehicleSpecSrvRequest Request;
typedef MoraiVehicleSpecSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoraiVehicleSpecSrv
} // namespace morai_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::morai_msgs::MoraiVehicleSpecSrv > {
  static const char* value()
  {
    return "00e763d6a7313045c7676986f63a8fd8";
  }

  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrv&) { return value(); }
};

template<>
struct DataType< ::morai_msgs::MoraiVehicleSpecSrv > {
  static const char* value()
  {
    return "morai_msgs/MoraiVehicleSpecSrv";
  }

  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrv&) { return value(); }
};


// service_traits::MD5Sum< ::morai_msgs::MoraiVehicleSpecSrvRequest> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiVehicleSpecSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiVehicleSpecSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiVehicleSpecSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiVehicleSpecSrvRequest> should match
// service_traits::DataType< ::morai_msgs::MoraiVehicleSpecSrv >
template<>
struct DataType< ::morai_msgs::MoraiVehicleSpecSrvRequest>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiVehicleSpecSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::morai_msgs::MoraiVehicleSpecSrvResponse> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiVehicleSpecSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiVehicleSpecSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiVehicleSpecSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiVehicleSpecSrvResponse> should match
// service_traits::DataType< ::morai_msgs::MoraiVehicleSpecSrv >
template<>
struct DataType< ::morai_msgs::MoraiVehicleSpecSrvResponse>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiVehicleSpecSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiVehicleSpecSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_MORAIVEHICLESPECSRV_H
