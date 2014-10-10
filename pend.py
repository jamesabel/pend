
import argparse
import time

# todo: use glob

def main():
    description = 'Pend (as in "pending" or "wait") on one or more files to be written (i.e. each file must exist' \
                  ' and can be opened for reading).'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('files', nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose')
    parser.add_argument('-p', '--poll_time', default='0.2', help='time to wait between polls')
    parser.add_argument('-t', '--timeout', default=None, help='timeout (seconds)')
    args = parser.parse_args()

    poll_time = float(args.poll_time)
    if args.verbose:
        print('files', args.files)
        print('poll_time', poll_time)
        if args.timeout:
            print('timeout', args.timeout)
    pending = [True]
    start = time.time()
    while any(pending):
        pending = []
        for file_path in args.files:
            try:
                f = open(file_path, 'rb')
                f.close()
                pending.append(False)
            except:
                pending.append(True)
        if args.timeout:
            if (time.time() - start) >= float(args.timeout):
                print('timeout')
                pending = [False]
        if any(pending):
            #if args.verbose:
            #    print('pending', pending)
            time.sleep(poll_time)
        else:
            if args.verbose:
                print('done')

if __name__ == "__main__":
    main()
