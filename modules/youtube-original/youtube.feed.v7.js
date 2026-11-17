// Ken YouTube v7 feed-only bundle. Exact v6 wire filter; no playback/control change.
(function () {
  var req=typeof $request==='object'&&$request?$request:{};
  var res=typeof $response==='object'&&$response?$response:{};
  var match=/^https:\/\/youtubei\.googleapis\.com\/youtubei\/v1\/(browse|next|search)(?:\?.*)?$/.exec(String(req.url||''));
  var endpoint=match?match[1]:'';
  var body=res.bodyBytes==null?res.body:res.bodyBytes;
  var size=body==null?0:typeof body.byteLength==='number'?body.byteLength:typeof body.length==='number'?body.length:0;
  var statusRaw=res.status||res.statusCode||200,status=Number(statusRaw);
  if(!Number.isFinite(status)){var sm=/^\s*(?:HTTP\/\d(?:\.\d)?\s+)?(\d{3})\b/.exec(String(statusRaw));status=sm?Number(sm[1]):0;}
  function report(stage,count,reason){console.log('[KenYT v7-feed] endpoint='+endpoint+' stage='+stage+' bytes='+size+' status='+status+(count==null?'':' removed='+count)+(reason?' reason='+reason:''));}
  if(match)report('entry',null,'');
  if(!match||size<=0||size>1048576||status<200||status>=300){if(match)report('pass',null,size<=0?'empty':size>1048576?'size':'status');$done({});return;}
function kenFeedFilter(input, endpoint) {
  var roots = {"browse":0,"next":13,"search":16,"player":17,"get_watch":18}, schema = [{"9":2,"10":2},{"58174010":11},{"58173949":10,"49399797":7},{"1":-1},{"1":-1},{},{"51431404":4},{"1":8},{"50195462":3,"51845067":9},{"5":6},{"1":1},{"4":2},{"51779735":14},{"7":12,"8":2},{"1":2},{"50195462":3,"49399797":7},{"4":2,"7":15},{"7":-2,"68":-2},{"1":19},{"2":17,"3":13}];
  var b = input instanceof Uint8Array ? input : input instanceof ArrayBuffer ? new Uint8Array(input) : Array.isArray(input) ? new Uint8Array(input) : null;
  if (!b) throw new Error('unsupported binary body');
  var visits = 0, removed = 0;
  function u32(at, end) {
    var value = 0, power = 1, i = 0, c;
    do { if (at >= end || ++i > 5) throw new Error('bad varint'); c = b[at++]; value += (c & 127) * power; power *= 128; } while (c & 128);
    if (value > 4294967295) throw new Error('overflow');
    return [value, at];
  }
  function fields(start, end, fn) {
    var at = start;
    while (at < end) {
      if (++visits > 50000) throw new Error('field budget');
      var begin = at, tag = u32(at, end); at = tag[1];
      var no = Math.floor(tag[0] / 8), wire = tag[0] % 8, tagEnd = at, bodyStart = at, bodyEnd = at;
      if (!no) throw new Error('zero field');
      if (wire === 2) { var length = u32(at, end); bodyStart = length[1]; bodyEnd = bodyStart + length[0]; at = bodyEnd; }
      else if (wire === 0) { var j = 0, c; do { if (at >= end || ++j > 10) throw new Error('bad scalar'); c = b[at++]; } while (c & 128); bodyEnd = at; }
      else if (wire === 1) { at += 8; bodyEnd = at; }
      else if (wire === 5) { at += 4; bodyEnd = at; }
      else throw new Error('unsupported wire');
      if (at > end) throw new Error('truncated');
      fn({start:begin, end:at, tagEnd:tagEnd, no:no, wire:wire, bodyStart:bodyStart, bodyEnd:bodyEnd});
    }
  }
  function has(start, end, word) {
    outer: for (var at = start; at <= end - word.length; at++) {
      for (var j = 0; j < word.length; j++) if (b[at+j] !== word.charCodeAt(j)) continue outer;
      return true;
    }
    return false;
  }
  function child(range, no) {
    var result = null;
    if (range) fields(range[0],range[1],function(f){if (!result && f.no===no && f.wire===2) result=[f.bodyStart,f.bodyEnd];});
    return result;
  }
  function path(range, numbers) { for (var i=0; range && i<numbers.length; i++) range=child(range,numbers[i]); return range; }
  function adItem(start, end) {
    var ad = false;
    fields(start,end,function(f){
      if(f.wire===2 && f.no!==153515154 && has(f.bodyStart,f.bodyEnd,'pagead')) ad=true;
      if(f.wire!==2 || f.no!==153515154) return;
      var range=[f.bodyStart,f.bodyEnd];
      var eml=path(range,[172660663,2,183314536,1]);
      if(eml) {
        if(has(eml[0],eml[1],'inline_injection_entrypoint_layout.eml')) ad=true;
        // Match the upstream layout rule, not arbitrary title/caption text.
        var text=''; for(var i=eml[0];i<eml[1] && i<eml[0]+1024;i++) text+=String.fromCharCode(b[i]);
        if(/shorts(?!_pivot_item)/.test(text.split('|')[0])) ad=true;
      }
      var content=path(range,[172660663,1,168777401,5]);
      if(content) fields(content[0],content[1],function(g){if(g.wire===2 && g.no!==465160965 && has(g.bodyStart,g.bodyEnd,'pagead')) ad=true;});
    });
    return ad;
  }
  function varint(value) { var out=[]; do { var c=value%128;value=Math.floor(value/128);out.push(c+(value?128:0)); } while(value); return new Uint8Array(out); }
  function walk(start,end,type,depth) {
    if(depth>24) throw new Error('depth budget');
    var chunks=null, size=0, keep=start, map=schema[type];
    function append(x){chunks.push(x);size+=x.length;}
    fields(start,end,function(f){
      var target=map[f.no]; if(f.wire!==2 || target===undefined) return;
      var drop=target===-2 || (target===-1 && adItem(f.bodyStart,f.bodyEnd));
      var edited=target<0?null:walk(f.bodyStart,f.bodyEnd,target,depth+1);
      if(!drop && !edited) return;
      if(!chunks) chunks=[];
      if(f.start>keep) append(b.subarray(keep,f.start));
      if(drop) removed++;
      else { append(b.subarray(f.start,f.tagEnd));append(varint(edited.size));for(var i=0;i<edited.chunks.length;i++) append(edited.chunks[i]); }
      keep=f.end;
    });
    if(!chunks) return null;
    if(keep<end) append(b.subarray(keep,end));
    return {chunks:chunks,size:size};
  }
  var edited=walk(0,b.length,roots[endpoint],0);
  if(!edited) return {body:b,changed:false,removed:0};
  var out=new Uint8Array(edited.size), at=0;
  for(var i=0;i<edited.chunks.length;i++){out.set(edited.chunks[i],at);at+=edited.chunks[i].length;}
  return {body:out,changed:true,removed:removed};
}

  try {var result=kenFeedFilter(body,endpoint);report('wire-feed',result.removed,'');$done(result.changed?{body:result.body}:{});}
  catch(ignore){report('wire-feed-error',0,'');$done({});}
})();
