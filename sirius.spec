%define version 0.8.0
%define release 4mdk

Summary:	An othello chess game
Name:		sirius
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Boards
URL:		http://sirius.bitvis.nu/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source:		%{name}-%{version}.tar.bz2

BuildRequires:	libgnomeui2-devel
BuildRequires:	ImageMagick

%description
Sirius is a program for playing the game of othello. The program
includes an AI (Artificial Intelligence) opponent which plays at
a very challenging level and is actually quite hard to beat.
The AI opponent's strength can therefore be adjusted in several
ways to give you a suitable opponent.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ -z "%{buildroot}" -o "%{buildroot}" = "/" ] || rm -rf %{buildroot}
%makeinstall_std

# menu entry
mkdir -p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} << _EOF_
?package(%{name}): \
 command="%{_bindir}/sirius" \
 icon="%{name}.png" \
 longtitle="An othello chess" \
 needs="x11" \
 section="Amusement/Boards" \
 title="Sirius"
_EOF_

# icons
mkdir -p %{buildroot}%{_iconsdir} \
	 %{buildroot}%{_liconsdir} \
	 %{buildroot}%{_miconsdir}
convert -geometry 48x48 pixmaps/sirius.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 pixmaps/sirius.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 pixmaps/sirius.png %{buildroot}%{_miconsdir}/%{name}.png

%{find_lang} %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
[ -z "%{buildroot}" -o "%{buildroot}" = "/" ] || rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png