%global cartridgedir %{_libexecdir}/openshift/cartridges/elasticsearch

Summary:       Provides Elasticsearch support
Name:          openshift-cartridge-elasticsearch-med
Version:       1.0
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.elasticsearch.org
Source0:       %{name}-%{version}.tar.gz
Requires:      java-1.8.0-openjdk
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-elasticsearch-med-1.0 = 1.0.0
BuildArch:     noarch

%description
Provides Elasticsearch cartridge support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm -rf %{buildroot}%{cartridgedir}/rel-eng

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/env
%{cartridgedir}/lib
%{cartridgedir}/logs
%{cartridgedir}/metadata
%{cartridgedir}/template
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/README_pt.md
%doc %{cartridgedir}/LICENSE.txt

%changelog
* Mon Apr 09 2016 med 4 life <support@med4life.in> 1.0.0-1
- bump version (support@med4life.in)
- Update manifest.yml (support@med4life.in)
