%global tl_name obnov
%global tl_revision 33355

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Obyknovennaya Novaya fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/obnov
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/obnov.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/obnov.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Obyknovennaya Novaya (Ordinary New Face) typeface was widely used in
the USSR for scientific and technical publications, as well as
textbooks. The fonts are encoded to KOI8-R (which is a long-established
Russian font encoding, rather than a TeX/LaTeX encoding). To use the
fonts, the user needs Cyrillic font support.

