#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class triangolosmezzato(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "triangolosmezzato")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 64000

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_6_4 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 25000, 0.16057, 0, 0)
        self.analog_sig_source_x_1_6_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 23000, 0.15688, 0, 3.14)
        self.analog_sig_source_x_1_6_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 21000, 0.1929, 0, 0)
        self.analog_sig_source_x_1_6_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 19000, 0.1875, 0, 3.14)
        self.analog_sig_source_x_1_6_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 17000, 0.24151, 0, 0)
        self.analog_sig_source_x_1_6 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 15000, 0.23303, 0, 3.14)
        self.analog_sig_source_x_1_5 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 13000, 0.32260, 0, 0)
        self.analog_sig_source_x_1_4 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 11000, 0.307, 0, 3.14)
        self.analog_sig_source_x_1_3 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 9000, 0.4844, 0, 0)
        self.analog_sig_source_x_1_2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 7000, 0.4464, 0, 3.14)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 5000, 0.9584, 0, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 3000, 0.7328, 0, 3.14)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 8.6831, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 0, 3, 0, 3.14)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.analog_sig_source_x_1_2, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.analog_sig_source_x_1_3, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.analog_sig_source_x_1_4, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.analog_sig_source_x_1_5, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.analog_sig_source_x_1_6, 0), (self.blocks_add_xx_0, 8))
        self.connect((self.analog_sig_source_x_1_6_0, 0), (self.blocks_add_xx_0, 9))
        self.connect((self.analog_sig_source_x_1_6_1, 0), (self.blocks_add_xx_0, 10))
        self.connect((self.analog_sig_source_x_1_6_2, 0), (self.blocks_add_xx_0, 11))
        self.connect((self.analog_sig_source_x_1_6_3, 0), (self.blocks_add_xx_0, 12))
        self.connect((self.analog_sig_source_x_1_6_4, 0), (self.blocks_add_xx_0, 13))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "triangolosmezzato")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_5.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_6_4.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)




def main(top_block_cls=triangolosmezzato, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
