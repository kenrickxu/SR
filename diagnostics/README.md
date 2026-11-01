# Independent Shadowrocket diagnostics

`ABC-Diagnostic.conf` is a temporary, all-DIRECT comparison profile. It uses the system DNS upstream, requests real IP answers, and disables HTTPS decryption. It contains no proxy nodes, credentials, certificates, or subscription update URL.

## Test

1. Import it as a separate configuration. Do not overwrite CN, CNR, or another normal profile.
2. Record your enabled modules and temporarily disable them: modules can override a profile.
3. Select this profile, set Global Routing to Configuration, and use Proxy Type None for the comparison.
4. Reconnect Shadowrocket, then fully close and reopen the app being tested. Observe its initial network warning; no login or transaction is needed.
5. Restore your normal profile, modules, proxy type, and original settings, then reconnect.

This profile provides no overseas proxy access. DIRECT and real IP answers do not remove or hide the iOS VPN interface. Static review is not proof of successful phone import, runtime DNS behavior, or app compatibility.

CN, CNR, and Clash production profiles are independent of this file. Do not copy these diagnostic settings into a normal subscription as a presumed fix.
