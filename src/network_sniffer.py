from cicflowmeter.sniffer import create_sniffer
import sys
import os


sys.path.append(os.path.abspath('../'))
INPUT_INTERFACE = 'Wi-Fi'  # Change this to your network interface name
OUTPUT_FILE = os.path.join('traffic_data', 'flows.csv')

sniffer, session = create_sniffer(
    input_file=None,
    input_interface=INPUT_INTERFACE,
    output=OUTPUT_FILE,
    output_mode="csv",
)
sniffer.start()

try:
    sniffer.join()
except KeyboardInterrupt:
    sniffer.stop()
finally:
    # Stop periodic GC if present
    if hasattr(session, "_gc_stop"):
        session._gc_stop.set()
        session._gc_thread.join(timeout=2.0)
    sniffer.join()
    # Flush all flows at the end
    session.flush_flows()