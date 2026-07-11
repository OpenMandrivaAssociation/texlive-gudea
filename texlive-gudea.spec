%global tl_name gudea
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	The Gudea font face with support for LaTeX and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gudea
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gudea.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the Gudea family of fonts designed by Agustina
Mingote, with support for LaTeX and pdfLaTeX.

