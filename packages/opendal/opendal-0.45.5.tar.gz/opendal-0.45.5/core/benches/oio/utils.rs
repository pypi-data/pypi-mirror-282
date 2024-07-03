// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

use bytes::Bytes;
use opendal::raw::oio;
use opendal::*;
use rand::prelude::ThreadRng;
use rand::RngCore;

/// BlackHoleWriter will discard all data written to it so we can measure the buffer's cost.
pub struct BlackHoleWriter;

impl oio::Write for BlackHoleWriter {
    async fn write(&mut self, bs: Buffer) -> opendal::Result<usize> {
        Ok(bs.len())
    }

    async fn abort(&mut self) -> opendal::Result<()> {
        Ok(())
    }

    async fn close(&mut self) -> opendal::Result<()> {
        Ok(())
    }
}

pub fn gen_bytes(rng: &mut ThreadRng, size: usize) -> Bytes {
    let mut content = vec![0; size];
    rng.fill_bytes(&mut content);

    content.into()
}
