%global tl_name gudea
%global tl_revision 78931
%global tl_version 0.0.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	The Gudea font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gudea
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the Gudea family of fonts designed by Agustina
Mingote, with support for LaTeX and pdfLaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from gudea:
Map Gudea.map
TL_DROPIN_EOF
