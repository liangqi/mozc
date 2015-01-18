// Copyright 2010-2015, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//     * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//     * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef MOZC_RENDERER_UNIX_WINDOW_MANAGER_MOCK_H_
#define MOZC_RENDERER_UNIX_WINDOW_MANAGER_MOCK_H_

#include "renderer/unix/window_manager_interface.h"
#include "testing/base/public/gmock.h"

namespace mozc {
namespace renderer {
namespace gtk {

class WindowManagerMock : public WindowManagerInterface {
 public:
  MOCK_METHOD0(Initialize, void());
  MOCK_METHOD0(HideAllWindows, void());
  MOCK_METHOD0(ShowAllWindows, void());
  MOCK_METHOD1(UpdateLayout, void(const commands::RendererCommand &command));
  MOCK_METHOD0(Activate, bool());
  MOCK_CONST_METHOD0(IsAvailable, bool());
  MOCK_METHOD1(SetSendCommandInterface,
               bool(client::SendCommandInterface *send_command_interface));
  MOCK_METHOD2(SetWindowPos, void(int x, int y));
};

}  // namespace gtk
}  // namespace renderer
}  // namespace mozc

#endif  // MOZC_RENDERER_UNIX_WINDOW_MANAGER_MOCK_H_
