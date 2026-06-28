#!/usr/bin/env python3
"""mkpass — a small, dependency-free password generator.

Uses Python's `secrets` module for cryptographically strong randomness.
"""
import argparse
import math
import secrets
import string
import sys

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"


def build_charset(use_lower, use_upper, use_digits, use_symbols):
    """Assemble the character pool from the enabled classes."""
    classes = []
    if use_lower:
        classes.append(LOWER)
    if use_upper:
        classes.append(UPPER)
    if use_digits:
        classes.append(DIGITS)
    if use_symbols:
        classes.append(SYMBOLS)
    return "".join(classes)


def generate(length, charset):
    """Return a random password of `length` chars drawn from `charset`."""
    return "".join(secrets.choice(charset) for _ in range(length))


def entropy_bits(length, pool_size):
    """Estimate password entropy in bits for a uniform random draw."""
    if pool_size <= 1:
        return 0.0
    return length * math.log2(pool_size)


def parse_args(argv):
    p = argparse.ArgumentParser(
        prog="mkpass", description="Generate strong random passwords."
    )
    p.add_argument("-l", "--length", type=int, default=16,
                   help="password length (default: 16)")
    p.add_argument("-n", "--count", type=int, default=1,
                   help="how many to generate (default: 1)")
    p.add_argument("--no-lower", action="store_true",
                   help="exclude lowercase letters")
    p.add_argument("--no-upper", action="store_true",
                   help="exclude uppercase letters")
    p.add_argument("--no-digits", action="store_true",
                   help="exclude digits")
    p.add_argument("-s", "--symbols", action="store_true",
                   help="include punctuation symbols")
    p.add_argument("-e", "--entropy", action="store_true",
                   help="print estimated entropy to stderr")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.length < 1:
        print("error: length must be >= 1", file=sys.stderr)
        return 2
    charset = build_charset(
        not args.no_lower, not args.no_upper, not args.no_digits, args.symbols
    )
    if not charset:
        print("error: character set is empty; enable at least one class",
              file=sys.stderr)
        return 2
    if args.entropy:
        bits = entropy_bits(args.length, len(charset))
        print(f"# entropy: {bits:.1f} bits "
              f"(length {args.length}, pool {len(charset)})", file=sys.stderr)
    for _ in range(max(1, args.count)):
        print(generate(args.length, charset))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
