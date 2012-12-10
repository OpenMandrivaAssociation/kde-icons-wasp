%define base_name	kde-icons
%define theme_name	wasp
%define Theme_name	Wasp
%define version		2.6.1
%define name		%{base_name}-%{theme_name}
%define release		%mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wasp icon for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{Theme_name}.SVG.Icons-v%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=9763
Requires:	kdebase3-progs
Requires:   kdegraphics3-ksvg
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Wasp Icons for KDE (SVG & PNG)
 
Originally released on Gnome as apart of the Gnome Themes Extras Project.
Originally Worked by: Christian Schaller & Matthew McClintock
Converted, Modified, & Added to by: P.Yavitz
For more info view the README file.

NOTE: This theme comes with lots of wasp extras, Color-schemes,
Ksplash's, Wallpaper, GDM themes, & more...

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{Theme_name} 

%build
find -type f -exec chmod 644 {} \;

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/apps/kdisplay/color-schemes/
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/apps/kwin/icewm-themes/
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/%{theme_name}/
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/faces/

install -m 644 extras/kdm/user.png  $RPM_BUILD_ROOT/%{_datadir}/faces/user-wasp.png
install -m 644 extras/kdm/user_root.png  $RPM_BUILD_ROOT/%{_datadir}/faces/root-wasp.png
cp -r extras/color-scheme/*/{*.kcsrc,*.kcmrc} $RPM_BUILD_ROOT/%{_datadir}/apps/kdisplay/color-schemes/
cp -r extras/icewm/* $RPM_BUILD_ROOT/%{_datadir}/apps/kwin/icewm-themes/
cp -r extras/splash/Gonx $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/
cp -r extras/splash/Wasp $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/
cp -r extras/splash/WaspWare $RPM_BUILD_ROOT/%{_datadir}/apps/ksplash/Themes/
cp -r 16x16/ 22x22/ 32x32/ 48x48/ 64x64/ 128x128/ scalable/ index.desktop $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE 
%{_iconsdir}/%{theme_name}-%{version}/
%{_datadir}/apps/kdisplay/color-schemes/
%{_datadir}/apps/kwin/icewm-themes/
%{_datadir}/apps/ksplash/Themes/
%{_datadir}/faces/*.png


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.1-9mdv2011.0
+ Revision: 619904
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.6.1-8mdv2010.0
+ Revision: 438086
- rebuild

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.6.1-7mdv2009.1
+ Revision: 360341
- Fix Requires

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.6.1-6mdv2009.0
+ Revision: 240883
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.6.1-4mdv2008.0
+ Revision: 89437
- Fix Requires (Bug #33726)
- Import kde-icons-wasp




* Fri Jul 14 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.6.1-3mdv2007.0
- Rebuild
- Use mkrel

* Sun May 02 2004 Laurent Culioli <laurent@mandrake.org> 2.6.1-2mdk
- fix ksplash theme

* Mon Apr 19 2004 Laurent Culioli <laurent@mandrake.org> 2.6.1-1mdk
- new kde icon theme.
