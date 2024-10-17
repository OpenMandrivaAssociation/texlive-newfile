Name:		texlive-newfile
Version:	15878
Release:	2
Summary:	User level management of LaTeX input and output
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newfile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfile.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
