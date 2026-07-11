%global tl_name newfile
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	User level management of LaTeX input and output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newfile
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Commands are defined to manage the limited pool of input and output
handles provided by TeX. The streams so provided are mapped to various
of the LaTeX input and output mechanisms. Some facilities of the
verbatim package are also mapped.

