# TODO:
# - stop subpackages madness
#
# Conditional build:
%bcond_without	bs2b		# BS2B effect plugin
%bcond_with	jack1		# use JACK 1 (0.12x) instead of JACK 2 (1.9.x)
#
%define		audver	3.10
Summary:	Plugins for Audacious media player (metapackage)
Summary(pl.UTF-8):	Wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet)
Name:		audacious-plugins
Version:	3.10
Release:	2
License:	GPL v2+, LGPL v2+, GPL v3, MIT, BSD (see individual plugins)
Group:		X11/Applications/Sound
Source0:	http://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
# Source0-md5:	26268359f4f21171de35cc10d0545733
Patch0:		%{name}-verbose_make.patch
URL:		http://audacious-media-player.org/
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
# audacious-qt/qtaudio part
BuildRequires:	Qt5Multimedia-devel >= 5
# audacious-qt/gl-spectrum-qt part
BuildRequires:	Qt5OpenGL-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	adplug-devel
BuildRequires:	audacious-devel >= %{audver}
BuildRequires:	audacious-libs-gtk-devel >= %{audver}
BuildRequires:	audacious-libs-qt-devel >= %{audver}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig
### for plugins
# visualization-gl-spectrum
BuildRequires:	OpenGL-GLX-devel
# output-sdlout (could be also SDL-devel >= 1.2.11)
BuildRequires:	SDL2-devel >= 2.0
# input-amidi (>= 1.0), output-alsa (>= 1.0.16)
BuildRequires:	alsa-lib-devel >= 1.0.16
# general-aosd
BuildRequires:	cairo-devel >= 1.2.4
# general-scrobbler
BuildRequires:	curl-devel >= 7.9.7
# input-flacng (>= 1.2.1), output-file (>= 1.1.3)
BuildRequires:	flac-devel >= 1.2.1
# input-aac
BuildRequires:	faad2-devel >= 2
# input-ffaudio (libavcodec >= 53.40.0, libavformat >= 53.21.0, libavutil >= 51.27.0)
BuildRequires:	ffmpeg-devel
# input-amidi
BuildRequires:	fluidsynth-devel >= 2.0.0
BuildRequires:	gdk-pixbuf2-devel >= 2.26
# AUD_COMMON_PROGS (>= 2.32), general-lyricwiki (>= 2.14), general-mpris2 (>= 2.30), transport-gio (>= 2.22)
BuildRequires:	glib2-devel >= 1:2.32
# general-hotkey
BuildRequires:	gtk+2-devel >= 2:2.24
# output-jack
%if %{with jack1}
BuildRequires:	jack-audio-connection-kit-devel < 1.0
BuildRequires:	jack-audio-connection-kit-devel >= 0.120.1
%else
BuildRequires:	jack-audio-connection-kit-devel >= 1.9.7
%endif
# output-file
BuildRequires:	lame-libs-devel
# input-adplug
BuildRequires:	libbinio-devel >= 1.4
# effect-bs2b
%{?with_bs2b:BuildRequires:	libbs2b-devel >= 3.0.0}
# input-cdaudio-ng
BuildRequires:	libcddb-devel >= 1.2.1
BuildRequires:	libcdio-devel >= 0.70
BuildRequires:	libcdio-paranoia-devel >= 0.70
# container-cuesheet
BuildRequires:	libcue-devel
# transport-mms
BuildRequires:	libmms-devel >= 0.3
# input-modplug
BuildRequires:	libmodplug-devel
# input-madplug
BuildRequires:	libmpg123-devel >= 1.12
# general-notify
BuildRequires:	libnotify-devel >= 0.7
# input-vorbis
BuildRequires:	libogg-devel >= 2:1.0
# effect-resample, effect-speed-pitch, output-jack
BuildRequires:	libsamplerate-devel
# input-sid
BuildRequires:	libsidplayfp-devel >= 1.0
# input-sndfile
BuildRequires:	libsndfile-devel >= 0.19
# -std=gnu++11
BuildRequires:	libstdc++-devel >= 6:4.7
# input-vorbis (>= 1.0), output-file
BuildRequires:	libvorbis-devel >= 1:1.0
# container-xspf
BuildRequires:	libxml2-devel >= 2.0
# general-lirc
BuildRequires:	lirc-devel
# transport-neon
BuildRequires:	neon-devel >= 0.27
# general-aosd
BuildRequires:	pango-devel >= 1:1.14.7
# output-pulseaudio
BuildRequires:	pulseaudio-devel >= 0.9.9
# effect-sox-resampler
BuildRequires:	soxr-devel
# input-wavpack
BuildRequires:	wavpack-devel >= 4.31
# visualization-gl-spectrum
BuildRequires:	xorg-lib-libX11-devel
# general-aosd (aosd-xcomp option)
BuildRequires:	xorg-lib-libXcomposite-devel
# general-aosd
BuildRequires:	xorg-lib-libXrender-devel
# input-console
BuildRequires:	zlib-devel
Requires:	audacious-container-asx = %{version}-%{release}
Requires:	audacious-container-cuesheet = %{version}-%{release}
Requires:	audacious-container-m3u = %{version}-%{release}
Requires:	audacious-container-pl = %{version}-%{release}
Requires:	audacious-container-pls = %{version}-%{release}
Requires:	audacious-container-xspf = %{version}-%{release}
Requires:	audacious-effect-audiocompress = %{version}-%{release}
%{?with_bs2b:Requires:	audacious-effect-bs2b = %{version}-%{release}}
Requires:	audacious-effect-crossfade = %{version}-%{release}
Requires:	audacious-effect-crystalizer = %{version}-%{release}
Requires:	audacious-effect-echo = %{version}-%{release}
Requires:	audacious-effect-ladspa = %{version}-%{release}
Requires:	audacious-effect-mixer = %{version}-%{release}
Requires:	audacious-effect-resample = %{version}-%{release}
Requires:	audacious-effect-sox-resampler = %{version}-%{release}
Requires:	audacious-effect-speed-pitch = %{version}-%{release}
Requires:	audacious-effect-stereo = %{version}-%{release}
Requires:	audacious-effect-voice_removal = %{version}-%{release}
Requires:	audacious-general-alarm = %{version}-%{release}
Requires:	audacious-general-albumart = %{version}-%{release}
Requires:	audacious-general-aosd = %{version}-%{release}
Requires:	audacious-general-cd-menu-items = %{version}-%{release}
Requires:	audacious-general-hotkey = %{version}-%{release}
Requires:	audacious-general-lirc = %{version}-%{release}
Requires:	audacious-general-lyricwiki = %{version}-%{release}
Requires:	audacious-general-mpris2 = %{version}-%{release}
Requires:	audacious-general-notify = %{version}-%{release}
Requires:	audacious-general-scrobbler = %{version}-%{release}
Requires:	audacious-general-search-tool = %{version}-%{release}
Requires:	audacious-general-skins = %{version}-%{release}
Requires:	audacious-general-song-change = %{version}-%{release}
Requires:	audacious-general-statusicon = %{version}-%{release}
Requires:	audacious-input-aac = %{version}-%{release}
Requires:	audacious-input-adplug = %{version}-%{release}
Requires:	audacious-input-amidi = %{version}-%{release}
Requires:	audacious-input-cdaudio-ng = %{version}-%{release}
Requires:	audacious-input-console = %{version}-%{release}
Requires:	audacious-input-ffaudio = %{version}-%{release}
Requires:	audacious-input-flacng = %{version}-%{release}
Requires:	audacious-input-madplug = %{version}-%{release}
Requires:	audacious-input-metronom = %{version}-%{release}
Requires:	audacious-input-modplug = %{version}-%{release}
Requires:	audacious-input-psf2 = %{version}-%{release}
Requires:	audacious-input-sid = %{version}-%{release}
Requires:	audacious-input-sndfile = %{version}-%{release}
Requires:	audacious-input-tonegen = %{version}-%{release}
Requires:	audacious-input-vorbis = %{version}-%{release}
Requires:	audacious-input-vtx = %{version}-%{release}
Requires:	audacious-input-wavpack = %{version}-%{release}
Requires:	audacious-input-xsf = %{version}-%{release}
Requires:	audacious-output-alsa = %{version}-%{release}
Requires:	audacious-output-file = %{version}-%{release}
Requires:	audacious-output-jack = %{version}-%{release}
Requires:	audacious-output-pulseaudio = %{version}-%{release}
Requires:	audacious-output-sdlout = %{version}-%{release}
Requires:	audacious-transport-gio = %{version}-%{release}
Requires:	audacious-transport-mms = %{version}-%{release}
Requires:	audacious-transport-neon = %{version}-%{release}
Requires:	audacious-visualization-blur-scope = %{version}-%{release}
Requires:	audacious-visualization-cairo-spectrum = %{version}-%{release}
Requires:	audacious-visualization-gl-spectrum = %{version}-%{release}
Suggests:	audacious-general-gtkui = %{version}-%{release}
Suggests:	audacious-qt = %{version}-%{release}
Obsoletes:	bmp-extra-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Audacious media player (metapackage).

%description -l pl.UTF-8
Wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet).

%package -n audacious-container-asx
Summary:	Audacious media player - ASX container plugin
Summary(pl.UTF-8):	Wtyczka list ASX dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-asx
This plugin adds support for playlists in ASX format.

%description -n audacious-container-asx -l pl.UTF-8
Ta wtyczka dodaje obsługę list odtwarzania w formacie ASX.

%package -n audacious-container-cuesheet
Summary:	Audacious media player - cue container plugin
Summary(pl.UTF-8):	Wtyczka list cue dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-input-cuesheet
Obsoletes:	audacious-input-cuesheet_ng

%description -n audacious-container-cuesheet
Cue Sheet list plugin for Audacious media player.

%description -n audacious-container-cuesheet -l pl.UTF-8
Wtyczka list odtwarzania w formacie Cue Sheet dla dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-container-m3u
Summary:	Audacious media player - M3U container plugin
Summary(pl.UTF-8):	Wtyczka list M3U dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-m3u
This plugin adds support for playlists in M3U format.

%description -n audacious-container-m3u -l pl.UTF-8
Ta wtyczka dodaje obsługę list odtwarzania w formacie M3U.

%package -n audacious-container-pl
Summary:	Audacious media player - Audacious playlist format plugin
Summary(pl.UTF-8):	Wtyczka playlist dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-pl
This plugin adds support for Audacious playlists format.

%description -n audacious-container-pl -l pl.UTF-8
Ta wtyczka dodaje obsługę list odtwarzania w formacie własnym
odtwarzacza Audacious.

%package -n audacious-container-pls
Summary:	Audacious media player - PLS container plugin
Summary(pl.UTF-8):	Wtyczka list PLS dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-pls
This plugin adds support for playlists in PLS format.

%description -n audacious-container-pls -l pl.UTF-8
Ta wtyczka dodaje obsługę list odtwarzania w formacie PLS.

%package -n audacious-container-xspf
Summary:	Audacious media player - XSPF plugin
Summary(pl.UTF-8):	Wtyczka XSPF odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-xspf
This plugin adds support for playlists in XSPF format.

%description -n audacious-container-xspf -l pl.UTF-8
Ta wtyczka dodaje obsługę list odtwarzania w formacie XSPF.

%package -n audacious-effect-audiocompress
Summary:	Audacious media player - audiocompress plugin
Summary(pl.UTF-8):	Wtyczka audiocompress odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-audiocompress
Dynamic range compression plugin for Audacious media player.

%description -n audacious-effect-audiocompress -l pl.UTF-8
Wtyczka kompresji dynamiki dźwięku dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-effect-bs2b
Summary:	Audacious media player - BS2B effect plugin
Summary(pl.UTF-8):	Wtyczka efektu BS2B dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libbs2b >= 3.0.0

%description -n audacious-effect-bs2b
BS2B (Bauer stereophonic-to-binaural DSP) effect plugin for Audacious
media player.

%description -n audacious-effect-bs2b -l pl.UTF-8
Wtyczka efektu BS2B (DSP stereofoniczno-dwuusznego Bauera) dla
odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-crossfade
Summary:	Audacious media player - crossfade effect plugin
Summary(pl.UTF-8):	Wtyczka efektu crossfade dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	bmp-output-crossfade

%description -n audacious-effect-crossfade
Crossfade effect plugin for Audacious media player.

%description -n audacious-effect-crossfade -l pl.UTF-8
Wtyczka efektu crossfade dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-crystalizer
Summary:	Audacious media player - crystalizer plugin
Summary(pl.UTF-8):	Wtyczka crystalizer dla odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-crystalizer
crystalizer plugin for Audacious media player.

%description -n audacious-effect-crystalizer -l pl.UTF-8
Wtyczka crystalizer dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-echo
Summary:	Audacious media player - echo effect plugin
Summary(pl.UTF-8):	Wtyczka efektu echo dla odtwarzacza multimedialnego Audacious
License:	unknown
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-echo
echo effect plugin for Audacious media player.

%description -n audacious-effect-echo -l pl.UTF-8
Wtyczka efektu echo dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-ladspa
Summary:	Audacious media player - LADSPA host plugin
Summary(pl.UTF-8):	Wtyczka hosta LADSPA dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk >= %{audver}

%description -n audacious-effect-ladspa
LADSPA host plugin for Audacious media player. It allows to use LADSPA
plugins for effects in Audacious.

%description -n audacious-effect-ladspa -l pl.UTF-8
Wtyczka hosta LADSPA dla odtwarzacza multimedialnego Audacious.
Pozwala na używanie wtyczek LADSPA jako efektów w odtwarzaczu
Audacious.

%package -n audacious-effect-mixer
Summary:	Audacious media player - mixer plugin
Summary(pl.UTF-8):	Wtyczka mixer dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-mixer
Channel mixer plugin for Audacious media player.

%description -n audacious-effect-mixer -l pl.UTF-8
Wtyczka miksera kanałów dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-resample
Summary:	Audacious media player - resample plugin
Summary(pl.UTF-8):	Wtyczka resample dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-resample
Sample rate converter plugin for Audacious media player.

%description -n audacious-effect-resample -l pl.UTF-8
Wtyczka konwertera częstotliwości próbkowania dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-effect-sox-resampler
Summary:	Audacious media player - sox-resampler plugin
Summary(pl.UTF-8):	Wtyczka sox-resampler dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-sox-resampler
SoX based sample rate converter plugin for Audacious media player.

%description -n audacious-effect-sox-resampler -l pl.UTF-8
Oparta na SoX wtyczka konwertera częstotliwości próbkowania dla
odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-speed-pitch
Summary:	Audacious media player - speed-pitch plugin
Summary(pl.UTF-8):	Wtyczka speed-pitch dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-effect-sndstretch

%description -n audacious-effect-speed-pitch
Speed and pitch effect plugin for Audacious media player.

%description -n audacious-effect-speed-pitch -l pl.UTF-8
Wtyczka efektu odtwarzacza multimedialnego Audacious pozwalająca na
zmianę szybkości i wysokości dźwięków.

%package -n audacious-effect-stereo
Summary:	Audacious media player - stereo plugin
Summary(pl.UTF-8):	Wtyczka stereo dla odtwarzacza multimedialnego Audacious
License:	unknown
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-stereo
Stereo plugin for Audacious media player.

%description -n audacious-effect-stereo -l pl.UTF-8
Wtyczka stereo dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-voice_removal
Summary:	Audacious media player - voice_removal plugin
Summary(pl.UTF-8):	Wtyczka voice_removal dla odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-voice_removal
Voice removal plugin for Audacious media player.

%description -n audacious-effect-voice_removal -l pl.UTF-8
Wtyczka usuwająca głos dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-alarm
Summary:	Audacious media player - alarm plugin
Summary(pl.UTF-8):	Wtyczka alarm dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-general-alarm
Alarm plugin for Audacious media player.

%description -n audacious-general-alarm -l pl.UTF-8
Wtyczka budzika dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-albumart
Summary:	Audacious media player - albumart plugin
Summary(pl.UTF-8):	Wtyczka albumart dla odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-general-albumart
Album art plugin for Audacious media player.

%description -n audacious-general-albumart -l pl.UTF-8
Wtyczka prezentująca okładki albumów dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-general-aosd
Summary:	Audacious media player - aosd plugin
Summary(pl.UTF-8):	Wtyczka aosd dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	cairo >= 1.2.4
Requires:	pango >= 1:1.14.7

%description -n audacious-general-aosd
OSD (On-Screen Display) plugin for Audacious media player.

%description -n audacious-general-aosd -l pl.UTF-8
Wtyczka OSD (wyświetlacza na ekranie) dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-general-cd-menu-items
Summary:	Audacious media player - cd-menu-items plugin
Summary(pl.UTF-8):	Wtyczka cd-menu-items dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-cd-menu-items
CD menu items plugin for Audacious media player.

%description -n audacious-general-cd-menu-items -l pl.UTF-8
Wtyczka z menu odtwarzacza CD dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-general-gtkui
Summary:	Audacious media player - gtkui plugin
Summary(pl.UTF-8):	Wtyczka gtkui dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-general-gtkui
GTK+ UI lugin for Audacious media player.

%description -n audacious-general-gtkui -l pl.UTF-8
Wtyczka interfejsu graficznego GTK+ dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-qt
Summary:	Audacious media player - Qt related plugins
Summary(pl.UTF-8):	Wtyczki Qt dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-qt >= %{audver}

%description -n audacious-qt
Qt plugins for Audacious media player.

%description -n audacious-qt -l pl.UTF-8
Wtyczki związane z Qt dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-hotkey
Summary:	Audacious media player - hotkey plugin
Summary(pl.UTF-8):	Wtyczka hotkey dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}
Requires:	gtk+3 >= 3.0.0
Obsoletes:	bmp-general-xf86audio

%description -n audacious-general-hotkey
Global Hotkey plugin for Audacious media player. It allows to control
the player with global key combinations or multimedia keys.

%description -n audacious-general-hotkey -l pl.UTF-8
Wtyczka Global Hotkey dla odtwarzacza multimedialnego Audacious.
Pozwala na sterowanie odtwarzaczem przy użyciu globalnych kombinacji
klawiszy lub klawiszy multimedialnych.

%package -n audacious-general-lirc
Summary:	Audacious media player - lirc plugin
Summary(pl.UTF-8):	Wtyczka lirc dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	bmp-general-lirc

%description -n audacious-general-lirc
LIRC plugin for Audacious media player.

%description -n audacious-general-lirc -l pl.UTF-8
Wtyczka LIRC dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-lyricwiki
Summary:	Audacious media player - lyricwiki plugin
Summary(pl.UTF-8):	Wtyczka lyricwiki dla odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	glib2 >= 1:2.14

%description -n audacious-general-lyricwiki
LyricWiki plugin for Audacious media player.

%description -n audacious-general-lyricwiki -l pl.UTF-8
Wtyczka LyricWiki dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-mpris2
Summary:	Audacious media player - mpris2 plugin
Summary(pl.UTF-8):	Wtyczka mpris2 dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	glib2 >= 1:2.30

%description -n audacious-general-mpris2
MPRIS 2 server plugin for Audacious media player.

%description -n audacious-general-mpris2 -l pl.UTF-8
Wtyczka serwera MPRIS 2 dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-notify
Summary:	Audacious media player - notify plugin
Summary(pl.UTF-8):	Wtyczka notify dla odtwarzacza multimedialnego Audacious
License:	GPL v3+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}
Requires:	audacious-libs-qt >= %{audver}
Requires:	gdk-pixbuf2-devel >= 2.26
Requires:	libnotify >= 0.7

%description -n audacious-general-notify
Desktop notifications plugin for Audacious media player.

%description -n audacious-general-notify -l pl.UTF-8
Wtyczka powiadomień w środowisku graficznym dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-general-scrobbler
Summary:	Audacious media player - scrobbler plugin
Summary(pl.UTF-8):	Wtyczka scrobbler dla odtwarzacza multimedialnego Audacious
License:	unknown
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	curl-libs >= 7.9.7
Obsoletes:	bmp-general-audioscrobbler
Obsoletes:	bmp-general-scrobbler

%description -n audacious-general-scrobbler
Scrobbler plugin for Audacious media player.

%description -n audacious-general-scrobbler -l pl.UTF-8
Wtyczka scrobbler dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-search-tool
Summary:	Audacious media player - search tool plugin
Summary(pl.UTF-8):	Wtyczka wyszukiwania dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-general-search-tool
Song search tool plugin for Audacious media player.

%description -n audacious-general-search-tool -l pl.UTF-8
Wtyczka wyszukiwania utworu dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-skins
Summary:	Audacious media player - skins plugin
Summary(pl.UTF-8):	Wtyczka skins dla odtwarzacza multimedialnego Audacious
License:	GPL v3
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-general-skins
Skins plugin for Audacious media player.

%description -n audacious-general-skins -l pl.UTF-8
Wtyczka skórek dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-song-change
Summary:	Audacious media player - song change plugin
Summary(pl.UTF-8):	Wtyczka zmiany utworu dla odtwarzacza multimedialnego Audacious
License:	GPL v3
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-song-change
Song change plugin for Audacious media player.

%description -n audacious-general-song-change -l pl.UTF-8
Wtyczka zmiany utworu dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-statusicon
Summary:	Audacious media player - status icon plugin
Summary(pl.UTF-8):	Wtyczka ikonki statusu dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}
Obsoletes:	bmp-status-docklet

%description -n audacious-general-statusicon
Status icon plugin for Audacious media player.

%description -n audacious-general-statusicon -l pl.UTF-8
Wtyczka ikonki statusu dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-aac
Summary:	Audacious media player - AAC input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików AAC dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	faad2 >= 2

%description -n audacious-input-aac
AAC input plugin for Audacious media player.

%description -n audacious-input-aac -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do odtwarzania
plików AAC.

%package -n audacious-input-adplug
Summary:	Audacious media player - Adplug input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików Adplug dla odtwarzacza multimedialnego Audacious
License:	LGPL v2.1+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libbinio >= 1.4

%description -n audacious-input-adplug
Adplug input plugin for Audacious media player.

%description -n audacious-input-adplug -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do odtwarzania
plików Adplug.

%package -n audacious-input-amidi
Summary:	Audacious media player - midi input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików midi dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	alsa-lib >= 1.0
Requires:	audacious = %{audver}
Requires:	fluidsynth >= 2.0.0

%description -n audacious-input-amidi
ALSA midi input plugin for Audacious media player.

%description -n audacious-input-amidi -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
midi poprzez ALSA.

%package -n audacious-input-cdaudio-ng
Summary:	Audacious media player - cdaudio-ng input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa cdaudio-ng dla odtwarzacza multimedialnego Audacious
License:	GPL v3
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libcddb >= 1.2.1
Requires:	libcdio >= 0.70
Requires:	libcdio-paranoia >= 0.70
Obsoletes:	beep-media-player-input-cdaudio
Obsoletes:	bmp-input-cdaudio

%description -n audacious-input-cdaudio-ng
CD Digital Audio input plugin for Audacious media player.

%description -n audacious-input-cdaudio-ng -l pl.UTF-8
Wtyczka wejściowa odtwarzacza multimedialnego Audacious pozwalająca na
odtwarzanie płyt CD Digital Audio.

%package -n audacious-input-console
Summary:	Audacious media player - console input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików konsolowych odtwarzacza multimedialnego Audacious
License:	LGPL v2.1+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-console
Console Video Game Music (from 1980s, early 1990s) input plugin for
Audacious media player. It supports formats like AY, GBS, GYM, HES,
KSS, NSF/NSFE, SAP, SPC, VGM/VGZ.

%description -n audacious-input-console -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious pozwalająca na
odtwarzanie plików z muzyką do obsługi plików muzycznych z konsol do
gier z lat 1980 i wczesnych 1990. Obsługuje formaty takie jak AY, GBS,
GYM, HES, KSS, NSF/NSFE, SAP, SPC, VGM/VGZ.

%package -n audacious-input-ffaudio
Summary:	Audacious media player - ffaudio input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa ffaudio dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	bmp-input-mpc
Obsoletes:	bmp-input-mplayer
Obsoletes:	bmp-input-musepack

%description -n audacious-input-ffaudio
FFaudio input plugin for Audacious media player.

%description -n audacious-input-ffaudio -l pl.UTF-8
Wtyczka wejściowa ffaudio dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-flacng
Summary:	Audacious media player - FLAC input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików FLAC dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	flac >= 1.2.1

%description -n audacious-input-flacng
FLAC input plugin for Audacious media player.

%description -n audacious-input-flacng -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
FLAC.

%package -n audacious-input-metronom
Summary:	Audacious media player - metronom input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa metronom dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-metronom
Metronom (tact generator) input plugin for Audacious media player.

%description -n audacious-input-metronom -l pl.UTF-8
Wtyczka wejściowa metronom dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-madplug
Summary:	Audacious media player - madplug input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa madplug dla odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libmpg123 >= 1.12
Obsoletes:	beep-media-player-input-mpg123
Obsoletes:	bmp-input-mpg123

%description -n audacious-input-madplug
MPEG Audio Plugin for Audacious media player.

%description -n audacious-input-madplug -l pl.UTF-8
Wtyczka wejściowa madplug dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-modplug
Summary:	Audacious media player - modplug input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa modplug dla odtwarzacza multimedialnego Audacious
License:	Public Domain
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-modplug
modplug input plugin for Audacious media player.

%description -n audacious-input-modplug -l pl.UTF-8
Wtyczka wejściowa modplug dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-psf2
Summary:	Audacious media player - psf2 input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa psf2 dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-input-sexypsf
Obsoletes:	audacious-input-sexypsf

%description -n audacious-input-psf2
psf2 input plugin for Audacious media player.

%description -n audacious-input-psf2 -l pl.UTF-8
Wtyczka wejściowa psf2 dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-sid
Summary:	Audacious media player - SID input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa SID dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libsidplayfp >= 1.0

%description -n audacious-input-sid
SID input plugin for Audacious media player.

%description -n audacious-input-sid -l pl.UTF-8
Wtyczka wejściowa SID dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-sndfile
Summary:	Audacious media player - sndfile input plugin that uses libsndfile to read files
Summary(pl.UTF-8):	Wtyczka wejściowa sndfile dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libsndfile >= 0.19
Obsoletes:	beep-media-player-input-wav
Obsoletes:	bmp-input-wav

%description -n audacious-input-sndfile
sndfile is an input plugin for Audacious. Using sndfile extends the
capabilities of Audacious to open and play any file which can be
opened and read by libsndfile, including WAV, AIFF, AU, and SVX files
and many compressed version of these file formats.

%description -n audacious-input-sndfile -l pl.UTF-8
sndfile to wtyczka wejściowa dla Audacious-a. Jej użycie rozszerza
możliwości Audaciousa o otwieranie i odtwarzanie dowolnych plików,
które można otworzyć i odczytać przy pomocy biblioteki libsndfile, w
tym WAV, AIFF, AU i SVX oraz wiele skompresowanych wersji tych
formatów.

%package -n audacious-input-tonegen
Summary:	Audacious media player - tonegen input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa tonegen dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-tonegen
Input plugin to generate sound of given frequency for Audacious media
player.

%description -n audacious-input-tonegen -l pl.UTF-8
Wtyczka do generowania dźwięków o danej częstotliwości dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-input-vorbis
Summary:	Audacious media player - Vorbis input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa Vorbis dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libogg >= 2:1.0
Requires:	libvorbis >= 1:1.0
Obsoletes:	beep-media-player-input-vorbis
Obsoletes:	bmp-input-vorbis

%description -n audacious-input-vorbis
Vorbis input plugin for Audacious media player.

%description -n audacious-input-vorbis -l pl.UTF-8
Wtyczka wejściowa Vorbis dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-vtx
Summary:	Audacious media player - vtx input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa vtx dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	audacious-libs-gtk = %{audver}

%description -n audacious-input-vtx
vtx input plugin for Audacious media player.

%description -n audacious-input-vtx -l pl.UTF-8
Wtyczka wejściowa vtx dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-wavpack
Summary:	Audacious media player - WavPack input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa WavPack dla odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	wavpack-libs >= 4.31

%description -n audacious-input-wavpack
WavPack input plugin for Audacious media player.

%description -n audacious-input-wavpack -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
skompresowanych w formacie WavPack.

%package -n audacious-input-xsf
Summary:	Audacious media player - xsf input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików xsf dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-xsf
xsf input plugin for Audacious media player.

%description -n audacious-input-xsf -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
xsf.

%package -n audacious-output-alsa
Summary:	Audacious media player - ALSA output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa ALSA dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	alsa-lib >= 1.0.16
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin
Obsoletes:	beep-media-player-output-ALSA
Obsoletes:	beep-media-player-output-OSS
Obsoletes:	bmp-output-ALSA
Obsoletes:	bmp-output-OSS

%description -n audacious-output-alsa
Output ALSA plugin for Audacious media player.

%description -n audacious-output-alsa -l pl.UTF-8
Wtyczka wyjściowa ALSA dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-file
Summary:	Audacious media player - file-writer output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa zapisu do pliku dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	flac >= 1.1.3
Provides:	audacious-output-plugin
Obsoletes:	bmp-output-oggre

%description -n audacious-output-file
Output file-writer plugin for Audacious media player.

%description -n audacious-output-file -l pl.UTF-8
Wtyczka wyjściowa zapisu do pliku dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-output-jack
Summary:	Audacious media player - JACK output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa JACK dla odtwarzacza multimedialnego Audacious
License:	LGPL v2.1+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
%if %{with jack1}
Requires:	jack-audio-connection-kit-libs >= 0.120.1
%else
Requires:	jack-audio-connection-kit-libs >= 1.9.7
%endif
Provides:	audacious-output-plugin

%description -n audacious-output-jack
Output JACK plugin for Audacious media player.

%description -n audacious-output-jack -l pl.UTF-8
Wtyczka wyjściowa JACK dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-pulseaudio
Summary:	Audacious media player - PulseAudio output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	pulseaudio-libs >= 0.9.9
Provides:	audacious-output-plugin
Provides:	audacious-output-pulse_audio
Obsoletes:	audacious-output-pulse_audio
Obsoletes:	beep-media-player-output-esd
Obsoletes:	bmp-output-arts
Obsoletes:	bmp-output-esd

%description -n audacious-output-pulseaudio
PulseAudio output plugin for Audacious media player.

%description -n audacious-output-pulseaudio -l pl.UTF-8
Wtyczka wyjściowa PulseAudio dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-output-sdlout
Summary:	Audacious media player - sdlout output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa sdlout dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	SDL2 >= 2.0
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-sdlout
SDL output plugin for Audacious media player.

%description -n audacious-output-sdlout -l pl.UTF-8
Wtyczka wyjściowa SDL dla odtwarzacza multimedialnego Audacious.

%package -n audacious-transport-gio
Summary:	Audacious media player - gio transport plugin
Summary(pl.UTF-8):	Wtyczka transportu gio dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	glib2 >= 1:2.22
Provides:	audacious-transport-stdio
Obsoletes:	audacious-transport-smb
Obsoletes:	audacious-transport-stdio

%description -n audacious-transport-gio
GIO transport plugin for Audacious media player.

%description -n audacious-transport-gio -l pl.UTF-8
Wtyczka transportu GIO dla odtwarzacza multimedialnego Audacious.

%package -n audacious-transport-mms
Summary:	Audacious media player - MMS transport plugin
Summary(pl.UTF-8):	Wtyczka transportu MMS dla odtwarzacza multimedialnego Audacious
License:	BSD
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	libmms >= 0.3

%description -n audacious-transport-mms
This Audacious plugin adds support for mms:// streams.

%description -n audacious-transport-mms -l pl.UTF-8
Ta wtyczka odtwarzacza Audacious dodaje obsługę strumieni mms://.

%package -n audacious-transport-neon
Summary:	Audacious media player - neon transport plugin
Summary(pl.UTF-8):	Wtyczka transportu neon dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Requires:	neon >= 0.27

%description -n audacious-transport-neon
Neon HTTP/HTTPS transport plugin for Audacious media player.

%description -n audacious-transport-neon -l pl.UTF-8
Wtyczka transportu neon (HTTP/HTTPS) dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-visualization-blur-scope
Summary:	Audacious media player - Blur scope visualization plugin
Summary(pl.UTF-8):	Wtyczka wizualizacji Blur scope dla odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	bmp-visualization-blursk

%description -n audacious-visualization-blur-scope
Blur scope visualization plugin for Audacious media player.

%description -n audacious-visualization-blur-scope -l pl.UTF-8
Wtyczka wizualizacji Blur scope dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-visualization-cairo-spectrum
Summary:	Audacious media player - cairo-spectrum visualization plugin
Summary(pl.UTF-8):	Wtyczka wizualizacji cairo-spectrum odtwarzacza multimedialnego Audacious
License:	MIT
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-cairo-spectrum
Cairo spectrum analyzer visualization plugin for Audacious media
player.

%description -n audacious-visualization-cairo-spectrum -l pl.UTF-8
Oparta na Cairo wtyczka wizualizacji analizująca widmo dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-visualization-gl-spectrum
Summary:	Audacious media player - gl-spectrum visualization plugin
Summary(pl.UTF-8):	Wtyczka wizualizacji gl-spectrum odtwarzacza multimedialnego Audacious
License:	GPL v2+
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-gl-spectrum
OpenGL spectrum analyzer visualization plugin for Audacious media
player.

%description -n audacious-visualization-gl-spectrum -l pl.UTF-8
Oparta na OpenGL wtyczka wizualizacji analizująca widmo dla
odtwarzacza multimedialnego Audacious.

%prep
%setup -q
%patch0 -p1

while read file no; do
	head -n "$no" "$file" > $(dirname "$file")/LICENSE
done <<EOF
src/albumart/albumart.cc 19
src/alsa/alsa.cc 18
src/audpl/audpl.cc 18
src/cairo-spectrum/cairo-spectrum.cc 19
src/cd-menu-items/cd-menu-items.cc 18
src/compressor/compressor.cc 18
src/crossfade/crossfade.cc 18
src/cue/cue.cc 18
src/gio/gio.cc 18
src/mixer/mixer.cc 18
src/resample/resample.cc 18
src/sdlout/sdlout.cc 18
src/search-tool/search-tool.cc 18
src/gtkui/ui_gtk.cc 18
src/ladspa/plugin.cc 18
src/mpris2/plugin.cc 18
src/psf/plugin.cc 25
src/xsf/plugin.cc 25
src/crystalizer/crystalizer.cc 19
src/lyricwiki/lyricwiki.cc 19
src/voice_removal/voice_removal.cc 19
src/ffaudio/ffaudio-core.cc 19
src/mpg123/mpg123.cc 20
src/mms/mms.cc 18
EOF

# verbose build
sed -i '\,^.SILENT:,d' buildsys.mk.in

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	%{!?with_bs2b:--disable-bs2b} \
	--enable-amidiplug \
	--enable-qt \
	--enable-qtaudio

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/fa{_IR,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/id{_ID,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ml{_IN,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/pt{_PT,}
# outdated version of sr
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/sr_RS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/audacious/Effect/silence-removal.so
%attr(755,root,root) %{_libdir}/audacious/General/delete-files.so
%attr(755,root,root) %{_libdir}/audacious/General/playlist-manager.so
%attr(755,root,root) %{_libdir}/audacious/Output/oss4.so

%files -n audacious-container-asx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/asx.so
%attr(755,root,root) %{_libdir}/audacious/Container/asx3.so

%files -n audacious-container-cuesheet
%defattr(644,root,root,755)
%doc src/cue/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Container/cue.so

%files -n audacious-container-m3u
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/m3u.so

%files -n audacious-container-pl
%defattr(644,root,root,755)
%doc src/audpl/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Container/audpl.so

%files -n audacious-container-pls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/pls.so

%files -n audacious-container-xspf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/xspf.so

%files -n audacious-effect-audiocompress
%defattr(644,root,root,755)
%doc src/compressor/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/compressor.so

%if %{with bs2b}
%files -n audacious-effect-bs2b
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/bs2b.so
%endif

%files -n audacious-effect-crossfade
%defattr(644,root,root,755)
%doc src/crossfade/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/crossfade.so

%files -n audacious-effect-crystalizer
%defattr(644,root,root,755)
%doc src/crystalizer/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/crystalizer.so

%files -n audacious-effect-echo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/echo.so

%files -n audacious-effect-ladspa
%defattr(644,root,root,755)
%doc src/ladspa/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/ladspa.so

%files -n audacious-effect-mixer
%defattr(644,root,root,755)
%doc src/mixer/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/mixer.so

%files -n audacious-effect-resample
%defattr(644,root,root,755)
%doc src/resample/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/resample.so

%files -n audacious-effect-sox-resampler
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/sox-resampler.so

%files -n audacious-effect-speed-pitch
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/speed-pitch.so

%files -n audacious-effect-stereo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/stereo.so

%files -n audacious-effect-voice_removal
%defattr(644,root,root,755)
%doc src/voice_removal/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Effect/voice_removal.so

%files -n audacious-general-alarm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/alarm.so

%files -n audacious-general-albumart
%defattr(644,root,root,755)
%doc src/albumart/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/albumart.so

%files -n audacious-general-aosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/aosd.so

%files -n audacious-general-cd-menu-items
%defattr(644,root,root,755)
%doc src/cd-menu-items/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/cd-menu-items.so

%files -n audacious-general-gtkui
%defattr(644,root,root,755)
%doc src/gtkui/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/gtkui.so

%files -n audacious-general-hotkey
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/hotkey.so

%files -n audacious-general-lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/lirc.so

%files -n audacious-general-lyricwiki
%defattr(644,root,root,755)
%doc src/lyricwiki/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/lyricwiki.so

%files -n audacious-general-mpris2
%defattr(644,root,root,755)
%doc src/mpris2/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/mpris2.so

%files -n audacious-general-notify
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/notify.so

%files -n audacious-general-scrobbler
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/scrobbler.so

%files -n audacious-general-search-tool
%defattr(644,root,root,755)
%doc src/search-tool/LICENSE
%attr(755,root,root) %{_libdir}/audacious/General/search-tool.so

%files -n audacious-general-skins
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/skins.so
%{_datadir}/audacious/Skins

%files -n audacious-general-song-change
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/song_change.so

%files -n audacious-general-statusicon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/statusicon.so

%files -n audacious-input-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/aac-raw.so

%files -n audacious-input-adplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/adplug.so

%files -n audacious-input-amidi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/amidi-plug.so

%files -n audacious-input-cdaudio-ng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/cdaudio-ng.so

%files -n audacious-input-console
%defattr(644,root,root,755)
%doc src/console/gme_{design,notes,readme}.txt src/console/{notes,readme}.txt
%attr(755,root,root) %{_libdir}/audacious/Input/console.so

%files -n audacious-input-ffaudio
%defattr(644,root,root,755)
%doc src/ffaudio/{LICENSE,TODO}
%attr(755,root,root) %{_libdir}/audacious/Input/ffaudio.so

%files -n audacious-input-flacng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/flacng.so

%files -n audacious-input-madplug
%defattr(644,root,root,755)
%doc src/mpg123/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Input/madplug.so

%files -n audacious-input-metronom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/metronom.so

%files -n audacious-input-modplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/modplug.so

%files -n audacious-input-psf2
%defattr(644,root,root,755)
%doc src/psf/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Input/psf2.so

%files -n audacious-input-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/sid.so

%files -n audacious-input-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/sndfile.so

%files -n audacious-input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/tonegen.so

%files -n audacious-input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/vorbis.so

%files -n audacious-input-vtx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/vtx.so

%files -n audacious-input-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/wavpack.so

%files -n audacious-input-xsf
%defattr(644,root,root,755)
%doc src/xsf/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Input/xsf.so

%files -n audacious-output-alsa
%defattr(644,root,root,755)
%doc src/alsa/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Output/alsa.so

%files -n audacious-output-file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/filewriter.so

%files -n audacious-output-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/jack-ng.so

%files -n audacious-output-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/pulse_audio.so

%files -n audacious-output-sdlout
%defattr(644,root,root,755)
%doc src/sdlout/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Output/sdlout.so

%files -n audacious-transport-gio
%defattr(644,root,root,755)
%doc src/gio/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Transport/gio.so

%files -n audacious-transport-mms
%defattr(644,root,root,755)
%doc src/mms/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Transport/mms.so

%files -n audacious-transport-neon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Transport/neon.so

%files -n audacious-visualization-blur-scope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/blur_scope.so

%files -n audacious-visualization-cairo-spectrum
%defattr(644,root,root,755)
%doc src/cairo-spectrum/LICENSE
%attr(755,root,root) %{_libdir}/audacious/Visualization/cairo-spectrum.so

%files -n audacious-visualization-gl-spectrum
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/gl-spectrum.so

%files -n audacious-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/albumart-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/lyricwiki-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/playlist-manager-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/qtui.so
%attr(755,root,root) %{_libdir}/audacious/General/search-tool-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/skins-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/song-info-qt.so
%attr(755,root,root) %{_libdir}/audacious/General/statusicon-qt.so
%attr(755,root,root) %{_libdir}/audacious/Output/qtaudio.so
%attr(755,root,root) %{_libdir}/audacious/Visualization/gl-spectrum-qt.so
