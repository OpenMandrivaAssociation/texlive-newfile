# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/newfile
# catalog-date 2009-09-03 13:00:14 +0200
# catalog-license lppl
# catalog-version 1.0c
Name:		texlive-newfile
Version:	1.0c
Release:	2
Summary:	User level management of LaTeX input and output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newfile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Commands are defined to manage the limited pool of input and
output handles provided by TeX. The streams so provided are
mapped to various of the LaTeX input and output mechanisms.
Some facilities of the verbatim package are also mapped.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newfile/newfile.sty
%doc %{_texmfdistdir}/doc/latex/newfile/README
%doc %{_texmfdistdir}/doc/latex/newfile/newfile.pdf
#- source
%doc %{_texmfdistdir}/source/latex/newfile/newfile.dtx
%doc %{_texmfdistdir}/source/latex/newfile/newfile.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
