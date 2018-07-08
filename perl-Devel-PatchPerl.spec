#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-PatchPerl
Version  : 1.52
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Devel-PatchPerl-1.52.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Devel-PatchPerl-1.52.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdevel-patchperl-perl/libdevel-patchperl-perl_1.52-1.debian.tar.xz
Summary  : "Patch perl source a la Devel::PPPort's buildperl.pl"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-PatchPerl-bin
Requires: perl-Devel-PatchPerl-license
Requires: perl-Devel-PatchPerl-man
Requires: perl(File::pushd)
Requires: perl(Module::Pluggable)
BuildRequires : perl(File::pushd)
BuildRequires : perl(Module::Pluggable)

%description
NAME
Devel::PatchPerl - Patch perl source a la Devel::PPPort's buildperl.pl
VERSION

%package bin
Summary: bin components for the perl-Devel-PatchPerl package.
Group: Binaries
Requires: perl-Devel-PatchPerl-license
Requires: perl-Devel-PatchPerl-man

%description bin
bin components for the perl-Devel-PatchPerl package.


%package license
Summary: license components for the perl-Devel-PatchPerl package.
Group: Default

%description license
license components for the perl-Devel-PatchPerl package.


%package man
Summary: man components for the perl-Devel-PatchPerl package.
Group: Default

%description man
man components for the perl-Devel-PatchPerl package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Devel-PatchPerl-1.52
mkdir -p %{_topdir}/BUILD/Devel-PatchPerl-1.52/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Devel-PatchPerl-1.52/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Devel-PatchPerl
cp LICENSE %{buildroot}/usr/share/doc/perl-Devel-PatchPerl/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Devel/PatchPerl.pm
/usr/lib/perl5/site_perl/5.26.1/Devel/PatchPerl/Hints.pm
/usr/lib/perl5/site_perl/5.26.1/Devel/PatchPerl/Plugin.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/patchperl

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Devel-PatchPerl/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/patchperl.1
/usr/share/man/man3/Devel::PatchPerl.3
/usr/share/man/man3/Devel::PatchPerl::Hints.3
/usr/share/man/man3/Devel::PatchPerl::Plugin.3
