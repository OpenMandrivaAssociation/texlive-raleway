Name:		texlive-raleway
Version:	1.4
Release:	2
Summary:	Use Raleway with TeX(-alike) systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/raleway
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/raleway.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/raleway.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the Raleway family in an easy to use way.
For XeLaTeX and LuaLaTeX users the original OpenType fonts are
used. The entire font family is included.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/raleway
%{_texmfdistdir}/fonts/map/dvips/raleway
%{_texmfdistdir}/fonts/opentype/impallari/raleway
%{_texmfdistdir}/fonts/tfm/impallari/raleway
%{_texmfdistdir}/fonts/type1/impallari/raleway
%{_texmfdistdir}/fonts/vf/impallari/raleway
%{_texmfdistdir}/tex/latex/raleway
%doc %{_texmfdistdir}/doc/latex/raleway

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
