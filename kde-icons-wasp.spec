%define base_name	kde-icons
%define theme_name	wasp
%define Theme_name	Wasp
%define version		2.6.1
%define name		%{base_name}-%{theme_name}
%define release		%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wasp icon for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{Theme_name}.SVG.Icons-v%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=9763
Requires:	kdebase-progs
Requires:        kdegraphics-ksvg
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
