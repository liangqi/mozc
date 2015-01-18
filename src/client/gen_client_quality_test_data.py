# -*- coding: utf-8 -*-
# Copyright 2010-2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import codecs
import logging
import sys


def escape(string):
  return ''.join('\\x%02x' % ord(char) for char in string.encode('utf-8'))


def convert_tsv(filename):
  tsv = codecs.open(filename, 'rb', 'utf-8')
  for line in tsv:
    line = line.rstrip()
    if not line or line.startswith('#'):
      continue

    fields = line.split('\t')
    if len(fields) == 3:
      label = fields[0]
      expected = fields[1]
      query = fields[2]
    elif len(fields) < 6:
      logging.warning('invalid row format: %s', line)
      continue
    else:
      label = fields[0]
      expected = fields[4]
      query = fields[5]

    print '  // {"%s", "%s", "%s"},' % (label, expected, query)
    print ('  {"%s", "%s", "%s"},' %
           (escape(label), escape(expected), escape(query)))
  tsv.close()


def main():
  sys.stdin = codecs.getreader('utf-8')(sys.stdin)
  sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
  sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
  logging.basicConfig(level = logging.INFO)

  print '// Automatically generated by mozc'
  print '#ifndef MOZC_SESSION_QUALITY_MAIN_DATA_H_'
  print '#define MOZC_SESSION_QUALITY_MAIN_DATA_H_'
  print ''
  print 'namespace mozc {'
  print 'struct TestCase {'
  print '  const char* source;'
  print '  const char* expected_result;'
  print '  const char* hiragana_sentence;'
  print '};'
  print ''
  print 'static TestCase test_cases[] = {'

  for filename in sys.argv[1:]:
    convert_tsv(filename)

  print '  {NULL, NULL, NULL}'
  print '};'
  print '}  // namespace mozc'
  print '#endif  // MOZC_SESSION_QUALITY_MAIN_DATA_H_'


if __name__ == '__main__':
  main()
