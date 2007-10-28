# TODO: build plugin dependent on libprojectM
#
# Conditional build:
%bcond_with	gconf		# build with gconf support
%bcond_with	gnomevfs	# build with GNOME VFS support
#
%define		audver	1.3.2
Summary:	Plugins for Audacious media player (metapackage)
Summary(pl.UTF-8):	Wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet)
Name:		audacious-plugins
Version:	1.3.5
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://static.audacious-media-player.org/release/%{name}-%{version}.tgz
# Source0-md5:	ff6b5901367337f8149e15c8fb1fdf95
Source1:	mp3license
URL:		http://audacious-media-player.org/
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.6.0}
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	artsc-devel >= 0.9.5
BuildRequires:	audacious-devel >= %{audver}
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	esound-devel >= 0.2.8
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	fluidsynth-devel >= 1.0.6
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.6.0}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libbinio-devel >= 1.4
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel >= 0.3
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsidplay-devel
BuildRequires:	libsndfile-devel >= 0.19
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	lirc-devel
BuildRequires:	pango-devel >= 1.14.7
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.3
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	wavpack-devel >= 4.31
Requires:	audacious-container-m3u = %{version}-%{release}
Requires:	audacious-container-mms = %{version}-%{release}
Requires:	audacious-container-pls = %{version}-%{release}
Requires:	audacious-container-stdio = %{version}-%{release}
Requires:	audacious-container-xspf = %{version}-%{release}
Requires:	audacious-effect-audiocompress = %{version}-%{release}
Requires:	audacious-effect-echo = %{version}-%{release}
Requires:	audacious-effect-ladspa = %{version}-%{release}
Requires:	audacious-effect-sndstretch = %{version}-%{release}
Requires:	audacious-effect-stereo = %{version}-%{release}
Requires:	audacious-effect-voice_removal = %{version}-%{release}
Requires:	audacious-general-alarm = %{version}-%{release}
Requires:	audacious-general-aosd = %{version}-%{release}
Requires:	audacious-general-audioscrobbler = %{version}-%{release}
Requires:	audacious-general-curl = %{version}-%{release}
Requires:	audacious-general-evdev = %{version}-%{release}
Requires:	audacious-general-lirc = %{version}-%{release}
Requires:	audacious-general-song-change = %{version}-%{release}
Requires:	audacious-general-statusicon = %{version}-%{release}
Requires:	audacious-input-aac = %{version}-%{release}
Requires:	audacious-input-adplug = %{version}-%{release}
Requires:	audacious-input-alac = %{version}-%{release}
Requires:	audacious-input-amidi = %{version}-%{release}
Requires:	audacious-input-cdaudio = %{version}-%{release}
Requires:	audacious-input-console = %{version}-%{release}
Requires:	audacious-input-cuesheet = %{version}-%{release}
Requires:	audacious-input-flac = %{version}-%{release}
Requires:	audacious-input-madplug = %{version}-%{release}
Requires:	audacious-input-metronom = %{version}-%{release}
Requires:	audacious-input-modplug = %{version}-%{release}
Requires:	audacious-input-mpc = %{version}-%{release}
Requires:	audacious-input-sexypsf = %{version}-%{release}
Requires:	audacious-input-sid = %{version}-%{release}
Requires:	audacious-input-timidity = %{version}-%{release}
Requires:	audacious-input-tonegen = %{version}-%{release}
Requires:	audacious-input-tta = %{version}-%{release}
Requires:	audacious-input-vorbis = %{version}-%{release}
Requires:	audacious-input-vtx = %{version}-%{release}
Requires:	audacious-input-wav = %{version}-%{release}
Requires:	audacious-input-wavpack = %{version}-%{release}
Requires:	audacious-input-wma = %{version}-%{release}
Requires:	audacious-output-alsa = %{version}-%{release}
Requires:	audacious-output-arts = %{version}-%{release}
Requires:	audacious-output-disk = %{version}-%{release}
Requires:	audacious-output-esd = %{version}-%{release}
Requires:	audacious-output-jack = %{version}-%{release}
Requires:	audacious-output-lame = %{version}-%{release}
Requires:	audacious-output-null = %{version}-%{release}
Requires:	audacious-output-oss = %{version}-%{release}
Requires:	audacious-output-pulse_audio = %{version}-%{release}
Requires:	audacious-visualization-blur-scope = %{version}-%{release}
Requires:	audacious-visualization-paranormal = %{version}-%{release}
Requires:	audacious-visualization-rocklight = %{version}-%{release}
Requires:	audacious-visualization-rovascope = %{version}-%{release}
Requires:	audacious-visualization-spectrum = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Audacious media player (metapackage).

%description -l pl.UTF-8
Wtyczki dla odtwarzacza multimedialnego Audacious (metapakiet).

%package -n audacious-container-m3u
Summary:	Audacious media player - M3U plugin
Summary(pl.UTF-8):	Wtyczka M3U odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-m3u
This plugin adds support for playlists in M3U format.

%description -n audacious-container-m3u -l pl.UTF-8
Ta wtyczka dodaje wsparcie dla list odtwarzania w formacie M3U.

%package -n audacious-container-mms
Summary:	Audacious media player - MMS plugin
Summary(pl.UTF-8):	Wtyczka MMS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-mms
This plugin adds support for mms:// streams.

%description -n audacious-container-mms -l pl.UTF-8
Ta wtyczka dodaje wsparcie dla strumieni mms://.

%package -n audacious-container-pls
Summary:	Audacious media player - PLS plugin
Summary(pl.UTF-8):	Wtyczka PLS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-pls
This plugin adds support for playlists in PLS format.

%description -n audacious-container-pls -l pl.UTF-8
Ta wtyczka dodaje wsparcie dla list odtwarzania w formacie PLS.

%package -n audacious-container-stdio
Summary:	Audacious media player - STDIO plugin
Summary(pl.UTF-8):	Wtyczka STDIO odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-stdio
This plugin adds support for file:// streams.

%description -n audacious-container-stdio -l pl.UTF-8
Ta wtyczka dodaje wsparcie dla strumieni file://.

%package -n audacious-container-xspf
Summary:	Audacious media player - XSPF plugin
Summary(pl.UTF-8):	Wtyczka XSPF odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-container-xspf
This plugin adds support for playlists in XSPF format.

%description -n audacious-container-xspf -l pl.UTF-8
Ta wtyczka dodaje wsparcie dla list odtwarzania w formacie XSPF.

%package -n audacious-effect-audiocompress
Summary:	Audacious media player - audiocompress plugin
Summary(pl.UTF-8):	Wtyczka audiocompress odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-audiocompress
audiocompress plugin for Audacious media player.

%description -n audacious-effect-audiocompress -l pl.UTF-8
Wtyczka audiocompress dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-echo
Summary:	Audacious media player - echo plugin
Summary(pl.UTF-8):	Wtyczka echo odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-echo
echo plugin for Audacious media player.

%description -n audacious-effect-echo -l pl.UTF-8
Wtyczka echo dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-ladspa
Summary:	Audacious media player - LADSPA plugin
Summary(pl.UTF-8):	Wtyczka LADSPA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-ladspa
LADSPA plugin for Audacious media player.

%description -n audacious-effect-ladspa -l pl.UTF-8
Wtyczka LADSPA dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-sndstretch
Summary:	Audacious media player - sndstretch plugin
Summary(pl.UTF-8):	Wtyczka sndstretch odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-sndstretch
sndstretch plugin for Audacious media player.

%description -n audacious-effect-sndstretch -l pl.UTF-8
Wtyczka sndstretch dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-stereo
Summary:	Audacious media player - stereo plugin
Summary(pl.UTF-8):	Wtyczka stereo odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-stereo
stereo plugin for Audacious media player.

%description -n audacious-effect-stereo -l pl.UTF-8
Wtyczka stereo dla odtwarzacza multimedialnego Audacious.

%package -n audacious-effect-voice_removal
Summary:	Audacious media player - voice_removal plugin
Summary(pl.UTF-8):	Wtyczka voice_removal odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-effect-voice_removal
voice_removal plugin for Audacious media player.

%description -n audacious-effect-voice_removal -l pl.UTF-8
Wtyczka voice_removal dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-alarm
Summary:	Audacious media player - alarm plugin
Summary(pl.UTF-8):	Wtyczka alarm odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-alarm
alarm plugin for Audacious media player.

%description -n audacious-general-alarm -l pl.UTF-8
Wtyczka alarm dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-aosd
Summary:	Audacious media player - aosd plugin
Summary(pl.UTF-8):	Wtyczka aosd odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-aosd
aosd plugin for Audacious media player.

%description -n audacious-general-aosd -l pl.UTF-8
Wtyczka aosd dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-audioscrobbler
Summary:	Audacious media player - audioscrobbler.com plugin
Summary(pl.UTF-8):	Wtyczka odtwarzacza multimedialnego Audacious obsługująca serwis audioscrobbler.com
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-audioscrobbler
This plugin adds audioscrobbler.com profile support to Audacious media
player.

%description -n audacious-general-audioscrobbler -l pl.UTF-8
Ta wtyczka pozwala odtwarzaczowi multimedialnemu Audacious obsługiwać
profile audioscrobbler.com .

%package -n audacious-general-curl
Summary:	Audacious media player - curl plugin
Summary(pl.UTF-8):	Wtyczka curl odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-curl
Audacious media player - curl plugin.

%description -n audacious-general-curl -l pl.UTF-8
Wtyczka curl odtwarzacza multimedialnego Audacious.

%package -n audacious-general-evdev
Summary:	Audacious media player - evdev plugin
Summary(pl.UTF-8):	Wtyczka evdev odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-evdev
Audacious media player - evdev plugin.

%description -n audacious-general-evdev -l pl.UTF-8
Wtyczka evdev odtwarzacza multimedialnego Audacious.

%package -n audacious-general-lirc
Summary:	Audacious media player - LIRC plugin
Summary(pl.UTF-8):	Wtyczka LIRC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-lirc
LIRC plugin for Audacious media player.

%description -n audacious-general-lirc -l pl.UTF-8
Wtyczka LIRC dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-song-change
Summary:	Audacious media player - song change plugin
Summary(pl.UTF-8):	Wtyczka zmiany utworu odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-song-change
Song change plugin for Audacious media player.

%description -n audacious-general-song-change -l pl.UTF-8
Wtyczka zmiany utworu dla odtwarzacza multimedialnego Audacious.

%package -n audacious-general-statusicon
Summary:	Audacious media player - status icon plugin
Summary(pl.UTF-8):	Wtyczka ikonki statusu odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-general-statusicon
Status icon plugin for Audacious media player.

%description -n audacious-general-statusicon -l pl.UTF-8
Wtyczka ikonki statusu dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-aac
Summary:	Audacious media player - AAC input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików AAC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-aac
AAC input plugin for Audacious media player.

%description -n audacious-input-aac -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
AAC.

%package -n audacious-input-adplug
Summary:	Audacious media player - Adplug input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików Adplug odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-adplug
Adplug input plugin for Audacious media player.

%description -n audacious-input-adplug -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
Adplug.

%package -n audacious-input-alac
Summary:	Audacious media player - alac input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa alac odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-alac
alac input plugin for Audacious media player.

%description -n audacious-input-alac -l pl.UTF-8
Wtyczka wejściowa alac dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-amidi
Summary:	Audacious media player - midi input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików midi odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-amidi
ALSA midi input plugin for Audacious media player.

%description -n audacious-input-amidi -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
midi poprzez ALSA.

%package -n audacious-input-cdaudio
Summary:	Audacious media player - cdaudio input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa cdaudio odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-cdaudio
cdaudio input plugin for Audacious media player.

%description -n audacious-input-cdaudio -l pl.UTF-8
Wtyczka wejściowa cdaudio dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-console
Summary:	Audacious media player - console input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików konsolowych odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-input-sap

%description -n audacious-input-console
SPC, GYM, NSF, VGM and GBS input plugin for Audacious media player.

%description -n audacious-input-console -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
SPC, GYM, NSF, VGM i GBS.

%package -n audacious-input-cuesheet
Summary:	Audacious media player - cuesheet input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa cuesheet odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-cuesheet
cuesheet input plugin for Audacious media player.

%description -n audacious-input-cuesheet -l pl.UTF-8
Wtyczka wejściowa cuesheet dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-flac
Summary:	Audacious media player - FLAC input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików FLAC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-flac
FLAC input plugin for Audacious media player.

%description -n audacious-input-flac -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
FLAC.

%package -n audacious-input-metronom
Summary:	Audacious media player - metronom input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa metronom odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-metronom
metronom input plugin for Audacious media player.

%description -n audacious-input-metronom -l pl.UTF-8
Wtyczka wejściowa metronom dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-modplug
Summary:	Audacious media player - modplug input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa modplug odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-input-mikmod

%description -n audacious-input-modplug
modplug input plugin for Audacious media player.

%description -n audacious-input-modplug -l pl.UTF-8
Wtyczka wejściowa modplug dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-mpc
Summary:	Audacious media player - MPC input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa MPC odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-input-mikmod

%description -n audacious-input-mpc
This plugin for Audaciuos can play audio files which are encoded with
Andree Buschmann's encoder Musepack. These files have the filename
postfixes MPC, MP+ or MPP.

%description -n audacious-input-mpc -l pl.UTF-8
Ta wtyczka dla Audaciuos odtwarza pliki dźwiękowe zakodowane koderem
Musepack autorstwa Andree Buschmanna. Te pliki mają rozszerzenie MPC,
MP+ lub MPP.

%package -n audacious-input-madplug
Summary:	Audacious media player - madplug input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa madplug odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Obsoletes:	audacious-input-mpg123

%description -n audacious-input-madplug
madplug input plugin for Audacious media player.

%description -n audacious-input-madplug -l pl.UTF-8
Wtyczka wejściowa madplug dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-sexypsf
Summary:	Audacious media player - sexypsf input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa sexypsf odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-sexypsf
Playstation music input plugin for Audacious media player.

%description -n audacious-input-sexypsf -l pl.UTF-8
Wtyczka wejściowa do odgrywania plików muzycznych w formacie
Playstation dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-sid
Summary:	Audacious media player - SID input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa SID odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-sid
SID input plugin for Audacious media player.

%description -n audacious-input-sid -l pl.UTF-8
Wtyczka wejściowa SID dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-timidity
Summary:	Audacious media player - Timidity input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa Timidity odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-timidity
Timidity input plugin for Audacious media player.

%description -n audacious-input-timidity -l pl.UTF-8
Wtyczka wejściowa Timidity dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-tonegen
Summary:	Audacious media player - input plugin to generate sound of given frequency
Summary(pl.UTF-8):	Wtyczka do generowania dźwięków o danej częstotliwości odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-tonegen
Input plugin to generate sound of given frequency for Audacious media
player.

%description -n audacious-input-tonegen -l pl.UTF-8
Wtyczka do generowania dźwięków o danej częstotliwości dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-input-tta
Summary:	Audacious media player - input plugin to generate sound of given frequency
Summary(pl.UTF-8):	Wtyczka do generowania dźwięków o danej częstotliwości odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-tta
Input plugin to generate sound of given frequency for Audacious media
player.

%description -n audacious-input-tta -l pl.UTF-8
Wtyczka do generowania dźwięków o danej częstotliwości dla odtwarzacza
multimedialnego Audacious.

%package -n audacious-input-vorbis
Summary:	Audacious media player - Vorbis input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa Vorbis odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-vorbis
Vorbis input plugin for Audacious media player.

%description -n audacious-input-vorbis -l pl.UTF-8
Wtyczka wejściowa Vorbis dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-vtx
Summary:	Audacious media player - vtx input plugin
Summary(pl.UTF-8):	Wtyczka wejściowa vtx odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-vtx
vtx input plugin for Audacious media player.

%description -n audacious-input-vtx -l pl.UTF-8
Wtyczka wejściowa vtx dla odtwarzacza multimedialnego Audacious.

%package -n audacious-input-wav
Summary:	Audacious media player - WAV input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików WAV odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-wav
WAV input plugin for Audacious media player.

%description -n audacious-input-wav -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
WAV.

%package -n audacious-input-wavpack
Summary:	Audacious media player - WavPack input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania skompresowanych plików WAV odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-wavpack
WavPack input plugin for Audacious media player.

%description -n audacious-input-wavpack -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi
skompresowanych plików WAV.

%package -n audacious-input-wma
Summary:	Audacious media player - WMA input plugin
Summary(pl.UTF-8):	Wtyczka do odtwarzania plików WMA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-input-wma
WMA input plugin for Audacious media player.

%description -n audacious-input-wma -l pl.UTF-8
Wtyczka dla odtwarzacza multimedialnego Audacious do obsługi plików
WMA.

%package -n audacious-output-alsa
Summary:	Audacious media player - ALSA output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa ALSA odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin
Obsoletes:	audacious-output-ALSA

%description -n audacious-output-alsa
Output ALSA plugin for Audacious media player.

%description -n audacious-output-alsa -l pl.UTF-8
Wtyczka wyjściowa ALSA dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-arts
Summary:	Audacious media player - ARTS output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa ARTS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-arts
Output arts plugin for Audacious media player.

%description -n audacious-output-arts -l pl.UTF-8
Wtyczka wyjściowa arts dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-disk
Summary:	Audacious media player - disk-writer output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa zapisu na dysk odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-disk
Output disk-writer plugin for Audacious media player.

%description -n audacious-output-disk -l pl.UTF-8
Wtyczka wyjściowa zapisu na dysk dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-output-esd
Summary:	Audacious media player - esd output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa esd odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-esd
Output esd plugin for Audacious media player.

%description -n audacious-output-esd -l pl.UTF-8
Wtyczka wyjściowa esd dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-jack
Summary:	Audacious media player - JACK output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa JACK odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-jack
Output JACK plugin for Audacious media player.

%description -n audacious-output-jack -l pl.UTF-8
Wtyczka wyjściowa JACK dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-lame
Summary:	Audacious media player - lame output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa lame odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-lame
Output lame plugin for Audacious media player.

%description -n audacious-output-lame -l pl.UTF-8
Wtyczka wyjściowa lame dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-null
Summary:	Audacious media player - null output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa null odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-null
null output plugin for Audacious media player.

%description -n audacious-output-null -l pl.UTF-8
Wtyczka wyjściowa null dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-oss
Summary:	Audacious media player - OSS output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa OSS odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin
Obsoletes:	audacious-output-OSS

%description -n audacious-output-oss
Output OSS plugin for Audacious media player.

%description -n audacious-output-oss -l pl.UTF-8
Wtyczka wyjściowa OSS dla odtwarzacza multimedialnego Audacious.

%package -n audacious-output-pulse_audio
Summary:	Audacious media player - PulseAudio output plugin
Summary(pl.UTF-8):	Wtyczka wyjściowa PulseAudio odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}
Provides:	audacious-output-plugin

%description -n audacious-output-pulse_audio
PulseAudio output plugin for Audacious media player.

%description -n audacious-output-pulse_audio -l pl.UTF-8
Wtyczka wyjściowa PulseAudio dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-visualization-blur-scope
Summary:	Audacious media player - Blur scope visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna Blur scope odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-blur-scope
Blur scope visualization plugin for Audacious media player.

%description -n audacious-visualization-blur-scope -l pl.UTF-8
Wtyczka graficzna Blur scope dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-visualization-paranormal
Summary:	Audacious media player - Paranormal visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna Paranormal odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-paranormal
Paranormal visualization plugin for Audacious media player.

%description -n audacious-visualization-paranormal -l pl.UTF-8
Wtyczka graficzna Paranormal dla odtwarzacza multimedialnego
Audacious.

%package -n audacious-visualization-rocklight
Summary:	Audacious media player - Rocklight visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna Rocklight odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-rocklight
Rocklight visualization plugin for Audacious media player.

%description -n audacious-visualization-rocklight -l pl.UTF-8
Wtyczka graficzna Rocklight dla odtwarzacza multimedialnego Audacious.

%package -n audacious-visualization-rovascope
Summary:	Audacious media player - Rovascope visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna Rovascope odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-rovascope
Rovascope visualization plugin for Audacious media player.

%description -n audacious-visualization-rovascope -l pl.UTF-8
Wtyczka graficzna Rovascope dla odtwarzacza multimedialnego Audacious.

%package -n audacious-visualization-spectrum
Summary:	Audacious media player - Spectrum visualization plugin
Summary(pl.UTF-8):	Wtyczka graficzna Paranormal odtwarzacza multimedialnego Audacious
Group:		X11/Applications/Sound
Requires:	audacious = %{audver}

%description -n audacious-visualization-spectrum
Spectrum visualization plugin for Audacious media player.

%description -n audacious-visualization-spectrum -l pl.UTF-8
Wtyczka graficzna Spectrum dla odtwarzacza multimedialnego Audacious.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure \
	--%{?with_gconf:en}%{!?with_gconf:dis}able-gconf \
	--%{?with_gnomevfs:en}%{!?with_gnomevfs:dis}able-gnome-vfs \
	--enable-amidiplug \
	--enable-timidity

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/audacious/paranormal/Presets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/paranormal/Presets/*.pnv $RPM_BUILD_ROOT%{_datadir}/audacious/paranormal/Presets

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%files -n audacious-container-m3u
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/libm3u.so

%files -n audacious-container-mms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/libmms.so

%files -n audacious-container-pls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/libpls.so

%files -n audacious-container-stdio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/libstdio.so

%files -n audacious-container-xspf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Container/libxspf.so

%files -n audacious-effect-audiocompress
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libaudiocompress.so

%files -n audacious-effect-echo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libecho.so

%files -n audacious-effect-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libladspa.so

%files -n audacious-effect-sndstretch
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libsndstretch.so

%files -n audacious-effect-stereo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libstereo.so

%files -n audacious-effect-voice_removal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Effect/libvoice_removal.so

%files -n audacious-general-alarm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libalarm.so

%files -n audacious-general-aosd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libaosd.so

%files -n audacious-general-audioscrobbler
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libscrobbler.so
%{_datadir}/audacious/images/audioscrobbler*.png

%files -n audacious-general-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libcurl.so

%files -n audacious-general-evdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libevdev-plug.so

%files -n audacious-general-lirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/liblirc.so

%files -n audacious-general-song-change
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libsong_change.so

%files -n audacious-general-statusicon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/General/libstatusicon.so

%files -n audacious-input-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libaac.so

%files -n audacious-input-adplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libadplug.so

%files -n audacious-input-alac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libalac.so

%files -n audacious-input-amidi
%defattr(644,root,root,755)
%dir %{_libdir}/audacious/amidi-plug
%attr(755,root,root) %{_libdir}/audacious/amidi-plug/ap-alsa.so
%attr(755,root,root) %{_libdir}/audacious/amidi-plug/ap-dummy.so
%attr(755,root,root) %{_libdir}/audacious/amidi-plug/ap-fluidsynth.so
%attr(755,root,root) %{_libdir}/audacious/Input/libamidi-plug.so

%files -n audacious-input-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libcdaudio.so

%files -n audacious-input-console
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libconsole.so

%files -n audacious-input-cuesheet
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libcuesheet.so

%files -n audacious-input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libflac.so

%files -n audacious-input-mpc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmpc.so

%files -n audacious-input-madplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmadplug.so

%files -n audacious-input-metronom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmetronom.so

%files -n audacious-input-modplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libmodplug.so

%files -n audacious-input-sexypsf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libsexypsf.so

%files -n audacious-input-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libsid.so

%files -n audacious-input-timidity
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libtimidity.so

%files -n audacious-input-tonegen
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libtonegen.so

%files -n audacious-input-tta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libtta.so

%files -n audacious-input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libvorbis.so

%files -n audacious-input-vtx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libvtx.so

%files -n audacious-input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwav.so

%files -n audacious-input-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwavpack.so

%files -n audacious-input-wma
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Input/libwma.so

%files -n audacious-output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libALSA.so

%files -n audacious-output-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audacious-arts-helper
%attr(755,root,root) %{_libdir}/audacious/Output/libarts.so

%files -n audacious-output-disk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libdisk_writer.so

%files -n audacious-output-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libESD.so

%files -n audacious-output-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libjackout.so

%files -n audacious-output-lame
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/liblame.so

%files -n audacious-output-null
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libnull.so

%files -n audacious-output-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libOSS.so

%files -n audacious-output-pulse_audio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Output/libpulse_audio.so

%files -n audacious-visualization-blur-scope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libbscope.so

%files -n audacious-visualization-paranormal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libparanormal.so
%{_datadir}/audacious/paranormal

%files -n audacious-visualization-rocklight
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/librocklight.so

%files -n audacious-visualization-rovascope
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/librovascope.so

%files -n audacious-visualization-spectrum
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/audacious/Visualization/libspectrum.so
