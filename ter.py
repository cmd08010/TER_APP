import sys
import manage
from openadr.openadr import OPENADR


def main():
    sys.argv = ['manage.py', 'runserver', '0.0.0.0:8000']
    # print("ter.main() - starting OPENADR")
    adr = OPENADR()
    adr.start()
    # print("ter.main() - calling manage.main()")
    manage.main()
    # will never see this
    # print("ter.main() - called manage.main()")


if __name__ == '__main__':
    main()