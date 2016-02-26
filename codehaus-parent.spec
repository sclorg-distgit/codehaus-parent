%global pkg_name codehaus-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        4
Release:        5.11%{?dist}
Summary:        Parent pom file for codehaus projects

License:        ASL 2.0
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         %{pkg_name}-enforcer.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools


%description
This package contains the parent pom file for codehaus projects.


%prep
%setup -q -c -T -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%patch0
%{?scl:EOF}

%build


%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 codehaus-parent-%{version}.pom \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{pkg_name}.pom

%add_maven_depmap JPP-%{pkg_name}.pom 
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 4-5.11
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 4-5.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 4-5.9
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 4-5.8
- Mass rebuild 2015-01-13

* Wed Jan 07 2015 Michal Srb <msrb@redhat.com> - 4-5.7
- Migrate to .mfiles

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 4-5.6
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-5.5
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-5.4
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-5.3
- Mass rebuild 2014-02-18

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4-5
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4-3
- Install LICENSE

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 3 2012 Orion Poplawski <orion@cora.nwra.com> - 4-1
- Update to version 4

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3-5
- Patch enforcer plugin out so it's not needed in all child packages

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 5 2011 Orion Poplawski <orion@cora.nwra.com> - 3-3
- Strip requires

* Wed May 4 2011 Orion Poplawski <orion@cora.nwra.com> - 3-2
- Drop build and defattr
- Better summary/description
- Upstream set license to ASL 2.0

* Fri Apr 29 2011 Orion Poplawski <orion@cora.nwra.com> - 3-1
- Initial package
