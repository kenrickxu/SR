/* Ken Meituan splash response v3 Diagnostic (no filter behavior change). Known schema from blackmatrix7 startup.js.
 * No forwarding, storage, account fields or payload logging. Unknown shapes fail open.
 */
(function () {
  'use strict';
  var result = {}, reason = 'unchanged', removed = 0, shape = 'unread';
  function kind(v) { return v === null ? 'null' : Array.isArray(v) ? 'array' : typeof v; }
  function describe(obj) {
    var data = obj && obj.data;
    var code = obj && Object.prototype.hasOwnProperty.call(obj, 'code') ?
      ((typeof obj.code === 'number' || typeof obj.code === 'string') ?
        (obj.code === 0 || obj.code === '0' ? 'zero' : 'nonzero') : 'other') : 'absent';
    var names = ['startpicture', 'startPicture', 'openscreen', 'openScreen', 'splash', 'splashAd', 'splash_ad', 'ad', 'ads', 'mk'];
    var counts = names.map(function () { return 0; });
    var queue = [{value: obj, depth: 0}], visited = 0, limited = 0;
    for (var i = 0; i < queue.length && i < 1024; i++) {
      var item = queue[i], value = item.value; visited++;
      if (!value || typeof value !== 'object') continue;
      names.forEach(function (name, index) {
        if (Object.prototype.hasOwnProperty.call(value, name)) counts[index]++;
      });
      var keys = Object.keys(value);
      if (item.depth >= 8) { if (keys.length) limited = 1; continue; }
      for (var j = 0; j < keys.length; j++) {
        var child = value[keys[j]];
        if (child && typeof child === 'object') {
          if (queue.length >= 1024) { limited = 1; break; }
          queue.push({value: child, depth: item.depth + 1});
        }
      }
    }
    return 'root=' + kind(obj) + ' data=' + kind(data) + ' code=' + code +
      ' known=' + counts.join(',') + ' nodes=' + visited + ' limited=' + limited;
  }
  try {
    var url = String($request.url || '');
    if (!/^https?:\/\/(?:www|wmapi)\.meituan\.com\/api\/v\d+\/(?:appstatus|loadInfo)(?:\?|$)/.test(url)) { reason = 'endpoint'; }
    else if (typeof $response.body !== 'string' || !$response.body.length) { reason = 'empty'; }
    else if ($response.body.length > 1048576) { reason = 'size'; }
    else if ($response.status && !/^(?:HTTP\/\S+\s+)?2\d\d(?:\s|$)/.test(String($response.status))) { reason = 'status'; }
    else {
      var obj = JSON.parse($response.body);
      shape = describe(obj);
      var data = obj && obj.data;
      var sp = data && data.startpicture;
      if (sp && typeof sp === 'object') {
        ['ad', 'mk'].forEach(function (key) {
          if (Object.prototype.hasOwnProperty.call(sp, key) && Array.isArray(sp[key]) && sp[key].length) {
            removed += sp[key].length;
            sp[key] = [];
          }
        });
        if (removed) { result = {body: JSON.stringify(obj)}; reason = 'cleaned'; }
        else { reason = 'no_known_ads'; }
      } else { reason = 'no_known_schema'; }
    }
  } catch (_) { reason = 'parse'; }
  console.log('[KenMT-v3] reason=' + reason + ' removed=' + removed + ' ' + shape);
  $done(result);
})();
