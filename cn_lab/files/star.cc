#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/csma-module.h"
#include "ns3/bridge-module.h"
#include "ns3/applications-module.h"
#include "ns3/mobility-module.h"
#include "ns3/netanim-module.h"

using namespace ns3;

int main()
{
    LogComponentEnable("UdpEchoClientApplication",
                       LOG_LEVEL_INFO);

    LogComponentEnable("UdpEchoServerApplication",
                       LOG_LEVEL_INFO);

    NodeContainer switchNode;
    switchNode.Create(1);

    NodeContainer pcNodes;
    pcNodes.Create(5);

    MobilityHelper mobility;
    mobility.SetMobilityModel(
        "ns3::ConstantPositionMobilityModel");

    mobility.Install(switchNode);
    mobility.Install(pcNodes);

    switchNode.Get(0)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(50,50,0));

    pcNodes.Get(0)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(50,20,0));

    pcNodes.Get(1)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(20,40,0));

    pcNodes.Get(2)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(80,40,0));

    pcNodes.Get(3)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(30,80,0));

    pcNodes.Get(4)
        ->GetObject<ConstantPositionMobilityModel>()
        ->SetPosition(Vector(70,80,0));

    InternetStackHelper internet;
    internet.Install(pcNodes);

    CsmaHelper csma;

    csma.SetChannelAttribute(
        "DataRate",
        StringValue("100Mbps"));

    csma.SetChannelAttribute(
        "Delay",
        TimeValue(NanoSeconds(6560)));

    NetDeviceContainer switchDevices;
    NetDeviceContainer pcDevices;

    for(uint32_t i = 0; i < 5; i++)
    {
        NodeContainer link;

        link.Add(switchNode.Get(0));
        link.Add(pcNodes.Get(i));

        NetDeviceContainer devices =
            csma.Install(link);

        switchDevices.Add(devices.Get(0));
        pcDevices.Add(devices.Get(1));
    }

    BridgeHelper bridge;

    bridge.Install(
        switchNode.Get(0),
        switchDevices);

    Ipv4AddressHelper address;

    address.SetBase(
        "10.0.0.0",
        "255.255.255.0");

    Ipv4InterfaceContainer interfaces =
        address.Assign(pcDevices);

    std::cout << "===== Star Topology ====="
              << std::endl;

    for(uint32_t i = 0; i < 5; i++)
    {
        std::cout << "PC-" << i+1
                  << " : "
                  << interfaces.GetAddress(i)
                  << std::endl;
    }

    uint16_t port = 9;

    UdpEchoServerHelper server(port);

    ApplicationContainer serverApp =
        server.Install(pcNodes.Get(4));

    serverApp.Start(Seconds(1.0));
    serverApp.Stop(Seconds(10.0));

    UdpEchoClientHelper client(
        interfaces.GetAddress(4),
        port);

    client.SetAttribute(
        "MaxPackets",
        UintegerValue(5));

    client.SetAttribute(
        "Interval",
        TimeValue(Seconds(1.0)));

    client.SetAttribute(
        "PacketSize",
        UintegerValue(1024));

    ApplicationContainer clientApp =
        client.Install(pcNodes.Get(0));

    clientApp.Start(Seconds(2.0));
    clientApp.Stop(Seconds(8.0));

    AnimationInterface anim(
        "star-topology.xml");

    anim.UpdateNodeDescription(
        switchNode.Get(0),
        "Ethernet Switch");

    for(uint32_t i = 0; i < 5; i++)
    {
        std::string name =
            "PC-" + std::to_string(i+1);

        anim.UpdateNodeDescription(
            pcNodes.Get(i),
            name);
    }

    Simulator::Stop(Seconds(10.0));

    Simulator::Run();

    Simulator::Destroy();

    return 0;
}