%define version 0.8.0
%define release %mkrel 8

Summary:	An othello chess game
Name:		sirius
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Boards
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		https://sirius.bitvis.nu/

Source:		%{name}-%{version}.tar.bz2
Patch0:		sirius-0.8.0-fix-desktop-file.patch

BuildRequires:	libgnomeui2-devel
BuildRequires:	imagemagick

%description
Sirius is a program for playing the game of othello. The program
includes an AI (Artificial Intelligence) opponent which plays at
a very challenging level and is actually quite hard to beat.
The AI opponent's strength can therefore be adjusted in several
ways to give you a suitable opponent.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
[ -z "%{buildroot}" -o "%{buildroot}" = "/" ] || rm -rf %{buildroot}
%makeinstall_std

# icons
mkdir -p %{buildroot}%{_iconsdir} \
	 %{buildroot}%{_liconsdir} \
	 %{buildroot}%{_miconsdir}
convert -geometry 48x48 pixmaps/sirius.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 pixmaps/sirius.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 pixmaps/sirius.png %{buildroot}%{_miconsdir}/%{name}.png

%{find_lang} %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ -z "%{buildroot}" -o "%{buildroot}" = "/" ] || rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
