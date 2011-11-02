Name:		texlive-newfile
Version:	1.0c
Release:	1
Summary:	User level management of LaTeX input and output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newfile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Commands are defined to manage the limited pool of input and
output handles provided by TeX. The streams so provided are
mapped to various of the LaTeX input and output mechanisms.
Some facilities of the verbatim package are also mapped.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
