Name:		texlive-gudea
Version:	57359
Release:	1
Summary:	The Gudea font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gudea
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the Gudea family of fonts designed by
Agustina Mingote, with support for LaTeX and pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gudea
%{_texmfdistdir}/fonts/vf/public/gudea
%{_texmfdistdir}/fonts/type1/public/gudea
%{_texmfdistdir}/fonts/tfm/public/gudea
%{_texmfdistdir}/fonts/map/dvips/gudea
%{_texmfdistdir}/fonts/enc/dvips/gudea
%doc %{_texmfdistdir}/doc/fonts/gudea

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
