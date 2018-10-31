#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC68B494DF56ACC7E (info@bro.org)
#
Name     : bro
Version  : 2.5.5
Release  : 2
URL      : https://www.bro.org/downloads/bro-2.5.5.tar.gz
Source0  : https://www.bro.org/downloads/bro-2.5.5.tar.gz
Source99 : https://www.bro.org/downloads/bro-2.5.5.tar.gz.asc
Summary  : The Bro Client Communications Library
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-4.0 NCSA
Requires: bro-bin = %{version}-%{release}
Requires: bro-data = %{version}-%{release}
Requires: bro-license = %{version}-%{release}
Requires: bro-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : flex
BuildRequires : glibc-dev
BuildRequires : gperf
BuildRequires : gperftools
BuildRequires : gperftools-dev
BuildRequires : libpcap-dev
BuildRequires : openssl-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : swig
BuildRequires : zlib-dev
Patch1: CVE-2018-16807.patch

%description
Broccoli enables your applications to speak the Bro communication protocol,
allowing you to compose, send, request, and receive events. You can register
your own event handlers. You can talk to other Broccoli applications or Bro
agents -- Bro agents cannot tell whether they are talking to another
Bro or a Broccoli application. Communications can be SSL-encrypted. Broccoli
turns Bro into a distributed policy-controlled event management system.

%package bin
Summary: bin components for the bro package.
Group: Binaries
Requires: bro-data = %{version}-%{release}
Requires: bro-license = %{version}-%{release}
Requires: bro-man = %{version}-%{release}

%description bin
bin components for the bro package.


%package data
Summary: data components for the bro package.
Group: Data

%description data
data components for the bro package.


%package dev
Summary: dev components for the bro package.
Group: Development
Requires: bro-bin = %{version}-%{release}
Requires: bro-data = %{version}-%{release}
Provides: bro-devel = %{version}-%{release}

%description dev
dev components for the bro package.


%package license
Summary: license components for the bro package.
Group: Default

%description license
license components for the bro package.


%package man
Summary: man components for the bro package.
Group: Default

%description man
man components for the bro package.


%prep
%setup -q -n bro-2.5.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541029672
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541029672
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bro
cp COPYING %{buildroot}/usr/share/package-licenses/bro/COPYING
cp aux/binpac/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_binpac_COPYING
cp aux/bro-aux/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_bro-aux_COPYING
cp aux/bro-aux/plugin-support/skeleton/COPYING.edit-me %{buildroot}/usr/share/package-licenses/bro/aux_bro-aux_plugin-support_skeleton_COPYING.edit-me
cp aux/broccoli/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broccoli_COPYING
cp aux/broccoli/bindings/broccoli-python/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broccoli_bindings_broccoli-python_COPYING
cp aux/broccoli/bindings/broccoli-ruby/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broccoli_bindings_broccoli-ruby_COPYING
cp aux/broctl/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broctl_COPYING
cp aux/broctl/aux/capstats/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broctl_aux_capstats_COPYING
cp aux/broctl/aux/pysubnettree/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broctl_aux_pysubnettree_COPYING
cp aux/broctl/aux/trace-summary/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broctl_aux_trace-summary_COPYING
cp aux/broker/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_broker_COPYING
cp aux/btest/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_btest_COPYING
cp aux/netcontrol-connectors/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_netcontrol-connectors_COPYING
cp aux/plugins/elasticsearch/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_elasticsearch_COPYING
cp aux/plugins/kafka/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_kafka_COPYING
cp aux/plugins/myricom/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_myricom_COPYING
cp aux/plugins/netmap/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_netmap_COPYING
cp aux/plugins/pf_ring/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_pf_ring_COPYING
cp aux/plugins/redis/COPYING %{buildroot}/usr/share/package-licenses/bro/aux_plugins_redis_COPYING
cp doc/LICENSE %{buildroot}/usr/share/package-licenses/bro/doc_LICENSE
pushd clr-build
%make_install
popd
## install_append content
rm -f %{buildroot}/usr/include/binpac.h.in
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/binpac
/usr/bin/bro
/usr/bin/bro-config

%files data
%defattr(-,root,root,-)
/usr/share/bro/base/bif/__load__.bro
/usr/share/bro/base/bif/analyzer.bif.bro
/usr/share/bro/base/bif/bloom-filter.bif.bro
/usr/share/bro/base/bif/bro.bif.bro
/usr/share/bro/base/bif/broxygen.bif.bro
/usr/share/bro/base/bif/cardinality-counter.bif.bro
/usr/share/bro/base/bif/comm.bif.bro
/usr/share/bro/base/bif/const.bif.bro
/usr/share/bro/base/bif/data.bif.bro
/usr/share/bro/base/bif/event.bif.bro
/usr/share/bro/base/bif/file_analysis.bif.bro
/usr/share/bro/base/bif/input.bif.bro
/usr/share/bro/base/bif/logging.bif.bro
/usr/share/bro/base/bif/messaging.bif.bro
/usr/share/bro/base/bif/pcap.bif.bro
/usr/share/bro/base/bif/plugins/Bro_ARP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_AsciiReader.ascii.bif.bro
/usr/share/bro/base/bif/plugins/Bro_AsciiWriter.ascii.bif.bro
/usr/share/bro/base/bif/plugins/Bro_BackDoor.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_BenchmarkReader.benchmark.bif.bro
/usr/share/bro/base/bif/plugins/Bro_BinaryReader.binary.bif.bro
/usr/share/bro/base/bif/plugins/Bro_BitTorrent.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_ConnSize.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_ConnSize.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DCE_RPC.consts.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DCE_RPC.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DCE_RPC.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DHCP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DNP3.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_DNS.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FTP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FTP.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_File.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FileEntropy.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FileExtract.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FileExtract.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_FileHash.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Finger.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_GSSAPI.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_GTPv1.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Gnutella.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_HTTP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_HTTP.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_ICMP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_IMAP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_IRC.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Ident.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_InterConn.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_KRB.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_KRB.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Login.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Login.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_MIME.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Modbus.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_MySQL.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NCP.consts.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NCP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NTLM.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NTLM.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NTP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NetBIOS.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NetBIOS.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_NoneWriter.none.bif.bro
/usr/share/bro/base/bif/plugins/Bro_PE.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_POP3.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RADIUS.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RDP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RDP.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RFB.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RPC.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_RawReader.raw.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SIP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.consts.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_check_directory.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_close.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_create_directory.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_echo.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_logoff_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_negotiate.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_nt_cancel.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_nt_create_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_query_information.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_read_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_session_setup_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_transaction.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_transaction2.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_tree_connect_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_tree_disconnect.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_com_write_andx.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb1_events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_close.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_create.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_negotiate.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_read.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_session_setup.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_set_info.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_tree_connect.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_tree_disconnect.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_com_write.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.smb2_events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMB.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMTP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SMTP.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SNMP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SNMP.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SOCKS.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SQLiteReader.sqlite.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SQLiteWriter.sqlite.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SSH.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SSH.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SSL.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SSL.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SSL.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_SteppingStone.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Syslog.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_TCP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_TCP.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Teredo.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_UDP.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Unified2.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_Unified2.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_X509.events.bif.bro
/usr/share/bro/base/bif/plugins/Bro_X509.functions.bif.bro
/usr/share/bro/base/bif/plugins/Bro_X509.types.bif.bro
/usr/share/bro/base/bif/plugins/Bro_XMPP.events.bif.bro
/usr/share/bro/base/bif/plugins/__load__.bro
/usr/share/bro/base/bif/reporter.bif.bro
/usr/share/bro/base/bif/stats.bif.bro
/usr/share/bro/base/bif/store.bif.bro
/usr/share/bro/base/bif/strings.bif.bro
/usr/share/bro/base/bif/top-k.bif.bro
/usr/share/bro/base/bif/types.bif.bro
/usr/share/bro/base/files/extract/__load__.bro
/usr/share/bro/base/files/extract/main.bro
/usr/share/bro/base/files/hash/__load__.bro
/usr/share/bro/base/files/hash/main.bro
/usr/share/bro/base/files/pe/__load__.bro
/usr/share/bro/base/files/pe/consts.bro
/usr/share/bro/base/files/pe/main.bro
/usr/share/bro/base/files/unified2/__load__.bro
/usr/share/bro/base/files/unified2/main.bro
/usr/share/bro/base/files/x509/__load__.bro
/usr/share/bro/base/files/x509/main.bro
/usr/share/bro/base/frameworks/analyzer/__load__.bro
/usr/share/bro/base/frameworks/analyzer/main.bro
/usr/share/bro/base/frameworks/broker/__load__.bro
/usr/share/bro/base/frameworks/broker/main.bro
/usr/share/bro/base/frameworks/broker/store.bro
/usr/share/bro/base/frameworks/cluster/__load__.bro
/usr/share/bro/base/frameworks/cluster/main.bro
/usr/share/bro/base/frameworks/cluster/nodes/logger.bro
/usr/share/bro/base/frameworks/cluster/nodes/manager.bro
/usr/share/bro/base/frameworks/cluster/nodes/proxy.bro
/usr/share/bro/base/frameworks/cluster/nodes/worker.bro
/usr/share/bro/base/frameworks/cluster/setup-connections.bro
/usr/share/bro/base/frameworks/communication/__load__.bro
/usr/share/bro/base/frameworks/communication/main.bro
/usr/share/bro/base/frameworks/control/__load__.bro
/usr/share/bro/base/frameworks/control/main.bro
/usr/share/bro/base/frameworks/dpd/__load__.bro
/usr/share/bro/base/frameworks/dpd/main.bro
/usr/share/bro/base/frameworks/files/__load__.bro
/usr/share/bro/base/frameworks/files/magic/__load__.bro
/usr/share/bro/base/frameworks/files/magic/archive.sig
/usr/share/bro/base/frameworks/files/magic/audio.sig
/usr/share/bro/base/frameworks/files/magic/font.sig
/usr/share/bro/base/frameworks/files/magic/general.sig
/usr/share/bro/base/frameworks/files/magic/image.sig
/usr/share/bro/base/frameworks/files/magic/libmagic.sig
/usr/share/bro/base/frameworks/files/magic/msoffice.sig
/usr/share/bro/base/frameworks/files/magic/video.sig
/usr/share/bro/base/frameworks/files/main.bro
/usr/share/bro/base/frameworks/input/__load__.bro
/usr/share/bro/base/frameworks/input/main.bro
/usr/share/bro/base/frameworks/input/readers/ascii.bro
/usr/share/bro/base/frameworks/input/readers/benchmark.bro
/usr/share/bro/base/frameworks/input/readers/binary.bro
/usr/share/bro/base/frameworks/input/readers/raw.bro
/usr/share/bro/base/frameworks/input/readers/sqlite.bro
/usr/share/bro/base/frameworks/intel/__load__.bro
/usr/share/bro/base/frameworks/intel/cluster.bro
/usr/share/bro/base/frameworks/intel/files.bro
/usr/share/bro/base/frameworks/intel/input.bro
/usr/share/bro/base/frameworks/intel/main.bro
/usr/share/bro/base/frameworks/logging/__load__.bro
/usr/share/bro/base/frameworks/logging/main.bro
/usr/share/bro/base/frameworks/logging/postprocessors/__load__.bro
/usr/share/bro/base/frameworks/logging/postprocessors/scp.bro
/usr/share/bro/base/frameworks/logging/postprocessors/sftp.bro
/usr/share/bro/base/frameworks/logging/writers/ascii.bro
/usr/share/bro/base/frameworks/logging/writers/none.bro
/usr/share/bro/base/frameworks/logging/writers/sqlite.bro
/usr/share/bro/base/frameworks/netcontrol/__load__.bro
/usr/share/bro/base/frameworks/netcontrol/catch-and-release.bro
/usr/share/bro/base/frameworks/netcontrol/cluster.bro
/usr/share/bro/base/frameworks/netcontrol/drop.bro
/usr/share/bro/base/frameworks/netcontrol/main.bro
/usr/share/bro/base/frameworks/netcontrol/non-cluster.bro
/usr/share/bro/base/frameworks/netcontrol/plugin.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/__load__.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/acld.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/broker.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/debug.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/openflow.bro
/usr/share/bro/base/frameworks/netcontrol/plugins/packetfilter.bro
/usr/share/bro/base/frameworks/netcontrol/shunt.bro
/usr/share/bro/base/frameworks/netcontrol/types.bro
/usr/share/bro/base/frameworks/notice/__load__.bro
/usr/share/bro/base/frameworks/notice/actions/add-geodata.bro
/usr/share/bro/base/frameworks/notice/actions/drop.bro
/usr/share/bro/base/frameworks/notice/actions/email_admin.bro
/usr/share/bro/base/frameworks/notice/actions/page.bro
/usr/share/bro/base/frameworks/notice/actions/pp-alarms.bro
/usr/share/bro/base/frameworks/notice/cluster.bro
/usr/share/bro/base/frameworks/notice/extend-email/hostnames.bro
/usr/share/bro/base/frameworks/notice/main.bro
/usr/share/bro/base/frameworks/notice/non-cluster.bro
/usr/share/bro/base/frameworks/notice/weird.bro
/usr/share/bro/base/frameworks/openflow/__load__.bro
/usr/share/bro/base/frameworks/openflow/cluster.bro
/usr/share/bro/base/frameworks/openflow/consts.bro
/usr/share/bro/base/frameworks/openflow/main.bro
/usr/share/bro/base/frameworks/openflow/non-cluster.bro
/usr/share/bro/base/frameworks/openflow/plugins/__load__.bro
/usr/share/bro/base/frameworks/openflow/plugins/broker.bro
/usr/share/bro/base/frameworks/openflow/plugins/log.bro
/usr/share/bro/base/frameworks/openflow/plugins/ryu.bro
/usr/share/bro/base/frameworks/openflow/types.bro
/usr/share/bro/base/frameworks/packet-filter/__load__.bro
/usr/share/bro/base/frameworks/packet-filter/cluster.bro
/usr/share/bro/base/frameworks/packet-filter/main.bro
/usr/share/bro/base/frameworks/packet-filter/netstats.bro
/usr/share/bro/base/frameworks/packet-filter/utils.bro
/usr/share/bro/base/frameworks/reporter/__load__.bro
/usr/share/bro/base/frameworks/reporter/main.bro
/usr/share/bro/base/frameworks/signatures/__load__.bro
/usr/share/bro/base/frameworks/signatures/main.bro
/usr/share/bro/base/frameworks/software/__load__.bro
/usr/share/bro/base/frameworks/software/main.bro
/usr/share/bro/base/frameworks/sumstats/__load__.bro
/usr/share/bro/base/frameworks/sumstats/cluster.bro
/usr/share/bro/base/frameworks/sumstats/main.bro
/usr/share/bro/base/frameworks/sumstats/non-cluster.bro
/usr/share/bro/base/frameworks/sumstats/plugins/__load__.bro
/usr/share/bro/base/frameworks/sumstats/plugins/average.bro
/usr/share/bro/base/frameworks/sumstats/plugins/hll_unique.bro
/usr/share/bro/base/frameworks/sumstats/plugins/last.bro
/usr/share/bro/base/frameworks/sumstats/plugins/max.bro
/usr/share/bro/base/frameworks/sumstats/plugins/min.bro
/usr/share/bro/base/frameworks/sumstats/plugins/sample.bro
/usr/share/bro/base/frameworks/sumstats/plugins/std-dev.bro
/usr/share/bro/base/frameworks/sumstats/plugins/sum.bro
/usr/share/bro/base/frameworks/sumstats/plugins/topk.bro
/usr/share/bro/base/frameworks/sumstats/plugins/unique.bro
/usr/share/bro/base/frameworks/sumstats/plugins/variance.bro
/usr/share/bro/base/frameworks/tunnels/__load__.bro
/usr/share/bro/base/frameworks/tunnels/main.bro
/usr/share/bro/base/init-bare.bro
/usr/share/bro/base/init-default.bro
/usr/share/bro/base/misc/find-checksum-offloading.bro
/usr/share/bro/base/misc/find-filtered-trace.bro
/usr/share/bro/base/misc/p0f.fp
/usr/share/bro/base/misc/version.bro
/usr/share/bro/base/protocols/conn/__load__.bro
/usr/share/bro/base/protocols/conn/contents.bro
/usr/share/bro/base/protocols/conn/inactivity.bro
/usr/share/bro/base/protocols/conn/main.bro
/usr/share/bro/base/protocols/conn/polling.bro
/usr/share/bro/base/protocols/conn/thresholds.bro
/usr/share/bro/base/protocols/dce-rpc/__load__.bro
/usr/share/bro/base/protocols/dce-rpc/consts.bro
/usr/share/bro/base/protocols/dce-rpc/dpd.sig
/usr/share/bro/base/protocols/dce-rpc/main.bro
/usr/share/bro/base/protocols/dhcp/__load__.bro
/usr/share/bro/base/protocols/dhcp/consts.bro
/usr/share/bro/base/protocols/dhcp/dpd.sig
/usr/share/bro/base/protocols/dhcp/main.bro
/usr/share/bro/base/protocols/dhcp/utils.bro
/usr/share/bro/base/protocols/dnp3/__load__.bro
/usr/share/bro/base/protocols/dnp3/consts.bro
/usr/share/bro/base/protocols/dnp3/dpd.sig
/usr/share/bro/base/protocols/dnp3/main.bro
/usr/share/bro/base/protocols/dns/__load__.bro
/usr/share/bro/base/protocols/dns/consts.bro
/usr/share/bro/base/protocols/dns/main.bro
/usr/share/bro/base/protocols/ftp/__load__.bro
/usr/share/bro/base/protocols/ftp/dpd.sig
/usr/share/bro/base/protocols/ftp/files.bro
/usr/share/bro/base/protocols/ftp/gridftp.bro
/usr/share/bro/base/protocols/ftp/info.bro
/usr/share/bro/base/protocols/ftp/main.bro
/usr/share/bro/base/protocols/ftp/utils-commands.bro
/usr/share/bro/base/protocols/ftp/utils.bro
/usr/share/bro/base/protocols/http/__load__.bro
/usr/share/bro/base/protocols/http/dpd.sig
/usr/share/bro/base/protocols/http/entities.bro
/usr/share/bro/base/protocols/http/files.bro
/usr/share/bro/base/protocols/http/main.bro
/usr/share/bro/base/protocols/http/utils.bro
/usr/share/bro/base/protocols/imap/__load__.bro
/usr/share/bro/base/protocols/imap/main.bro
/usr/share/bro/base/protocols/irc/__load__.bro
/usr/share/bro/base/protocols/irc/dcc-send.bro
/usr/share/bro/base/protocols/irc/dpd.sig
/usr/share/bro/base/protocols/irc/files.bro
/usr/share/bro/base/protocols/irc/main.bro
/usr/share/bro/base/protocols/krb/__load__.bro
/usr/share/bro/base/protocols/krb/consts.bro
/usr/share/bro/base/protocols/krb/dpd.sig
/usr/share/bro/base/protocols/krb/files.bro
/usr/share/bro/base/protocols/krb/main.bro
/usr/share/bro/base/protocols/modbus/__load__.bro
/usr/share/bro/base/protocols/modbus/consts.bro
/usr/share/bro/base/protocols/modbus/main.bro
/usr/share/bro/base/protocols/mysql/__load__.bro
/usr/share/bro/base/protocols/mysql/consts.bro
/usr/share/bro/base/protocols/mysql/main.bro
/usr/share/bro/base/protocols/ntlm/__load__.bro
/usr/share/bro/base/protocols/ntlm/main.bro
/usr/share/bro/base/protocols/pop3/__load__.bro
/usr/share/bro/base/protocols/pop3/dpd.sig
/usr/share/bro/base/protocols/radius/__load__.bro
/usr/share/bro/base/protocols/radius/consts.bro
/usr/share/bro/base/protocols/radius/main.bro
/usr/share/bro/base/protocols/rdp/__load__.bro
/usr/share/bro/base/protocols/rdp/consts.bro
/usr/share/bro/base/protocols/rdp/dpd.sig
/usr/share/bro/base/protocols/rdp/main.bro
/usr/share/bro/base/protocols/rfb/__load__.bro
/usr/share/bro/base/protocols/rfb/dpd.sig
/usr/share/bro/base/protocols/rfb/main.bro
/usr/share/bro/base/protocols/sip/__load__.bro
/usr/share/bro/base/protocols/sip/dpd.sig
/usr/share/bro/base/protocols/sip/main.bro
/usr/share/bro/base/protocols/smb/__load__.bro
/usr/share/bro/base/protocols/smb/const-dos-error.bro
/usr/share/bro/base/protocols/smb/const-nt-status.bro
/usr/share/bro/base/protocols/smb/consts.bro
/usr/share/bro/base/protocols/smtp/__load__.bro
/usr/share/bro/base/protocols/smtp/dpd.sig
/usr/share/bro/base/protocols/smtp/entities.bro
/usr/share/bro/base/protocols/smtp/files.bro
/usr/share/bro/base/protocols/smtp/main.bro
/usr/share/bro/base/protocols/snmp/__load__.bro
/usr/share/bro/base/protocols/snmp/main.bro
/usr/share/bro/base/protocols/socks/__load__.bro
/usr/share/bro/base/protocols/socks/consts.bro
/usr/share/bro/base/protocols/socks/dpd.sig
/usr/share/bro/base/protocols/socks/main.bro
/usr/share/bro/base/protocols/ssh/__load__.bro
/usr/share/bro/base/protocols/ssh/dpd.sig
/usr/share/bro/base/protocols/ssh/main.bro
/usr/share/bro/base/protocols/ssl/__load__.bro
/usr/share/bro/base/protocols/ssl/consts.bro
/usr/share/bro/base/protocols/ssl/dpd.sig
/usr/share/bro/base/protocols/ssl/files.bro
/usr/share/bro/base/protocols/ssl/main.bro
/usr/share/bro/base/protocols/ssl/mozilla-ca-list.bro
/usr/share/bro/base/protocols/syslog/__load__.bro
/usr/share/bro/base/protocols/syslog/consts.bro
/usr/share/bro/base/protocols/syslog/main.bro
/usr/share/bro/base/protocols/tunnels/__load__.bro
/usr/share/bro/base/protocols/tunnels/dpd.sig
/usr/share/bro/base/protocols/xmpp/__load__.bro
/usr/share/bro/base/protocols/xmpp/dpd.sig
/usr/share/bro/base/protocols/xmpp/main.bro
/usr/share/bro/base/utils/active-http.bro
/usr/share/bro/base/utils/addrs.bro
/usr/share/bro/base/utils/conn-ids.bro
/usr/share/bro/base/utils/dir.bro
/usr/share/bro/base/utils/directions-and-hosts.bro
/usr/share/bro/base/utils/email.bro
/usr/share/bro/base/utils/exec.bro
/usr/share/bro/base/utils/files.bro
/usr/share/bro/base/utils/geoip-distance.bro
/usr/share/bro/base/utils/json.bro
/usr/share/bro/base/utils/numbers.bro
/usr/share/bro/base/utils/paths.bro
/usr/share/bro/base/utils/patterns.bro
/usr/share/bro/base/utils/queue.bro
/usr/share/bro/base/utils/site.bro
/usr/share/bro/base/utils/strings.bro
/usr/share/bro/base/utils/thresholds.bro
/usr/share/bro/base/utils/time.bro
/usr/share/bro/base/utils/urls.bro
/usr/share/bro/broxygen/__load__.bro
/usr/share/bro/broxygen/example.bro
/usr/share/bro/policy/frameworks/communication/listen.bro
/usr/share/bro/policy/frameworks/control/controllee.bro
/usr/share/bro/policy/frameworks/control/controller.bro
/usr/share/bro/policy/frameworks/dpd/detect-protocols.bro
/usr/share/bro/policy/frameworks/dpd/packet-segment-logging.bro
/usr/share/bro/policy/frameworks/files/detect-MHR.bro
/usr/share/bro/policy/frameworks/files/entropy-test-all-files.bro
/usr/share/bro/policy/frameworks/files/extract-all-files.bro
/usr/share/bro/policy/frameworks/files/hash-all-files.bro
/usr/share/bro/policy/frameworks/intel/do_expire.bro
/usr/share/bro/policy/frameworks/intel/do_notice.bro
/usr/share/bro/policy/frameworks/intel/seen/__load__.bro
/usr/share/bro/policy/frameworks/intel/seen/conn-established.bro
/usr/share/bro/policy/frameworks/intel/seen/dns.bro
/usr/share/bro/policy/frameworks/intel/seen/file-hashes.bro
/usr/share/bro/policy/frameworks/intel/seen/file-names.bro
/usr/share/bro/policy/frameworks/intel/seen/http-headers.bro
/usr/share/bro/policy/frameworks/intel/seen/http-url.bro
/usr/share/bro/policy/frameworks/intel/seen/pubkey-hashes.bro
/usr/share/bro/policy/frameworks/intel/seen/smtp-url-extraction.bro
/usr/share/bro/policy/frameworks/intel/seen/smtp.bro
/usr/share/bro/policy/frameworks/intel/seen/ssl.bro
/usr/share/bro/policy/frameworks/intel/seen/where-locations.bro
/usr/share/bro/policy/frameworks/intel/seen/x509.bro
/usr/share/bro/policy/frameworks/intel/whitelist.bro
/usr/share/bro/policy/frameworks/packet-filter/shunt.bro
/usr/share/bro/policy/frameworks/signatures/detect-windows-shells.sig
/usr/share/bro/policy/frameworks/software/version-changes.bro
/usr/share/bro/policy/frameworks/software/vulnerable.bro
/usr/share/bro/policy/frameworks/software/windows-version-detection.bro
/usr/share/bro/policy/integration/barnyard2/__load__.bro
/usr/share/bro/policy/integration/barnyard2/main.bro
/usr/share/bro/policy/integration/barnyard2/types.bro
/usr/share/bro/policy/integration/collective-intel/__load__.bro
/usr/share/bro/policy/integration/collective-intel/main.bro
/usr/share/bro/policy/misc/capture-loss.bro
/usr/share/bro/policy/misc/detect-traceroute/__load__.bro
/usr/share/bro/policy/misc/detect-traceroute/detect-low-ttls.sig
/usr/share/bro/policy/misc/detect-traceroute/main.bro
/usr/share/bro/policy/misc/dump-events.bro
/usr/share/bro/policy/misc/known-devices.bro
/usr/share/bro/policy/misc/load-balancing.bro
/usr/share/bro/policy/misc/loaded-scripts.bro
/usr/share/bro/policy/misc/profiling.bro
/usr/share/bro/policy/misc/scan.bro
/usr/share/bro/policy/misc/stats.bro
/usr/share/bro/policy/misc/trim-trace-file.bro
/usr/share/bro/policy/misc/weird-stats.bro
/usr/share/bro/policy/protocols/conn/known-hosts.bro
/usr/share/bro/policy/protocols/conn/known-services.bro
/usr/share/bro/policy/protocols/conn/mac-logging.bro
/usr/share/bro/policy/protocols/conn/vlan-logging.bro
/usr/share/bro/policy/protocols/conn/weirds.bro
/usr/share/bro/policy/protocols/dhcp/known-devices-and-hostnames.bro
/usr/share/bro/policy/protocols/dns/auth-addl.bro
/usr/share/bro/policy/protocols/dns/detect-external-names.bro
/usr/share/bro/policy/protocols/ftp/detect-bruteforcing.bro
/usr/share/bro/policy/protocols/ftp/detect.bro
/usr/share/bro/policy/protocols/ftp/software.bro
/usr/share/bro/policy/protocols/http/detect-sqli.bro
/usr/share/bro/policy/protocols/http/detect-webapps.bro
/usr/share/bro/policy/protocols/http/detect-webapps.sig
/usr/share/bro/policy/protocols/http/header-names.bro
/usr/share/bro/policy/protocols/http/software-browser-plugins.bro
/usr/share/bro/policy/protocols/http/software.bro
/usr/share/bro/policy/protocols/http/var-extraction-cookies.bro
/usr/share/bro/policy/protocols/http/var-extraction-uri.bro
/usr/share/bro/policy/protocols/krb/ticket-logging.bro
/usr/share/bro/policy/protocols/modbus/known-masters-slaves.bro
/usr/share/bro/policy/protocols/modbus/track-memmap.bro
/usr/share/bro/policy/protocols/mysql/software.bro
/usr/share/bro/policy/protocols/rdp/indicate_ssl.bro
/usr/share/bro/policy/protocols/smb/__load__.bro
/usr/share/bro/policy/protocols/smb/dpd.sig
/usr/share/bro/policy/protocols/smb/files.bro
/usr/share/bro/policy/protocols/smb/main.bro
/usr/share/bro/policy/protocols/smb/smb1-main.bro
/usr/share/bro/policy/protocols/smb/smb2-main.bro
/usr/share/bro/policy/protocols/smtp/blocklists.bro
/usr/share/bro/policy/protocols/smtp/detect-suspicious-orig.bro
/usr/share/bro/policy/protocols/smtp/entities-excerpt.bro
/usr/share/bro/policy/protocols/smtp/software.bro
/usr/share/bro/policy/protocols/ssh/detect-bruteforcing.bro
/usr/share/bro/policy/protocols/ssh/geo-data.bro
/usr/share/bro/policy/protocols/ssh/interesting-hostnames.bro
/usr/share/bro/policy/protocols/ssh/software.bro
/usr/share/bro/policy/protocols/ssl/expiring-certs.bro
/usr/share/bro/policy/protocols/ssl/extract-certs-pem.bro
/usr/share/bro/policy/protocols/ssl/heartbleed.bro
/usr/share/bro/policy/protocols/ssl/known-certs.bro
/usr/share/bro/policy/protocols/ssl/log-hostcerts-only.bro
/usr/share/bro/policy/protocols/ssl/notary.bro
/usr/share/bro/policy/protocols/ssl/validate-certs.bro
/usr/share/bro/policy/protocols/ssl/validate-ocsp.bro
/usr/share/bro/policy/protocols/ssl/weak-keys.bro
/usr/share/bro/policy/tuning/__load__.bro
/usr/share/bro/policy/tuning/defaults/__load__.bro
/usr/share/bro/policy/tuning/defaults/extracted_file_limits.bro
/usr/share/bro/policy/tuning/defaults/packet-fragments.bro
/usr/share/bro/policy/tuning/defaults/warnings.bro
/usr/share/bro/policy/tuning/json-logs.bro
/usr/share/bro/policy/tuning/track-all-assets.bro
/usr/share/bro/site/local-logger.bro
/usr/share/bro/site/local-manager.bro
/usr/share/bro/site/local-proxy.bro
/usr/share/bro/site/local-worker.bro
/usr/share/bro/site/local.bro

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bro/COPYING
/usr/share/package-licenses/bro/aux_binpac_COPYING
/usr/share/package-licenses/bro/aux_bro-aux_COPYING
/usr/share/package-licenses/bro/aux_bro-aux_plugin-support_skeleton_COPYING.edit-me
/usr/share/package-licenses/bro/aux_broccoli_COPYING
/usr/share/package-licenses/bro/aux_broccoli_bindings_broccoli-python_COPYING
/usr/share/package-licenses/bro/aux_broccoli_bindings_broccoli-ruby_COPYING
/usr/share/package-licenses/bro/aux_broctl_COPYING
/usr/share/package-licenses/bro/aux_broctl_aux_capstats_COPYING
/usr/share/package-licenses/bro/aux_broctl_aux_pysubnettree_COPYING
/usr/share/package-licenses/bro/aux_broctl_aux_trace-summary_COPYING
/usr/share/package-licenses/bro/aux_broker_COPYING
/usr/share/package-licenses/bro/aux_btest_COPYING
/usr/share/package-licenses/bro/aux_netcontrol-connectors_COPYING
/usr/share/package-licenses/bro/aux_plugins_elasticsearch_COPYING
/usr/share/package-licenses/bro/aux_plugins_kafka_COPYING
/usr/share/package-licenses/bro/aux_plugins_myricom_COPYING
/usr/share/package-licenses/bro/aux_plugins_netmap_COPYING
/usr/share/package-licenses/bro/aux_plugins_pf_ring_COPYING
/usr/share/package-licenses/bro/aux_plugins_redis_COPYING
/usr/share/package-licenses/bro/doc_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/bro.8
