Name:		texlive-obnov
Version:	33355
Release:	2
Summary:	Obyknovennaya Novaya fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/obnov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/obnov.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/obnov.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Obyknovennaya Novaya (Ordinary New Face) typeface was
widely used in the USSR for scientific and technical
publications, as well as textbooks. The fonts are encoded to
KOI8-R (which is a long-established Russian font encoding,
rather than a TeX/LaTeX encoding). To use the fonts, the user
needs Cyrillic font support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/obnov/obn10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obn12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obn17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obn7.mf
%{_texmfdistdir}/fonts/source/public/obnov/obn_lcyw_code.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnb10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnb12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnb17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnb7.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnit10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnit12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnit17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnit7.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnitb10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnitb12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnitb17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsc10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsc12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsc17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsc7.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsl10.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsl12.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsl17.mf
%{_texmfdistdir}/fonts/source/public/obnov/obnsl7.mf
%{_texmfdistdir}/fonts/tfm/public/obnov/obn10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obn12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obn17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obn7.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnb10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnb12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnb17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnb7.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnit10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnit12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnit17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnit7.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnitb10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnitb12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnitb17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsc7.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsl17.tfm
%{_texmfdistdir}/fonts/tfm/public/obnov/obnsl7.tfm
%{_texmfdistdir}/tex/latex/obnov/lcyw.cmap
%{_texmfdistdir}/tex/latex/obnov/lcywobn.fd
%doc %{_texmfdistdir}/doc/fonts/obnov/README
%doc %{_texmfdistdir}/doc/fonts/obnov/example_obn.pdf
%doc %{_texmfdistdir}/doc/fonts/obnov/example_obn.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
