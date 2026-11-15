/* Ken Meituan splash response v2. Known schema from blackmatrix7 startup.js.
 * No forwarding, storage, account fields or payload logging. Unknown shapes fail open.
 */
(function () {
  'use strict';
  var result = {}, reason = 'unchanged', removed = 0;
  try {
    var url = String($request.url || '');
    if (!/^https?:\/\/(?:www|wmapi)\.meituan\.com\/api\/v\d+\/(?:appstatus|loadInfo)(?:\?|$)/.test(url)) { reason = 'endpoint'; }
    else if (typeof $response.body !== 'string' || !$response.body.length) { reason = 'empty'; }
    else if ($response.body.length > 1048576) { reason = 'size'; }
    else if ($response.status && !/^(?:HTTP\/\S+\s+)?2\d\d(?:\s|$)/.test(String($response.status))) { reason = 'status'; }
    else {
      var obj = JSON.parse($response.body);
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
  console.log('[KenMT-v2] reason=' + reason + ' removed=' + removed);
  $done(result);
})();
