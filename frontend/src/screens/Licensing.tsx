import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

import { asset } from "../lib/asset"
import { getSiteInfo, type SiteInfo } from "../lib/siteInfo"
import { LANGS, getLang, setLang, type Lang } from "../lib/dir"
import { useT } from "../lib/i18n"

const UPSTREAM_URL = "https://github.com/Kamra-PMS/kamra-pms"
const AGPL_URL = "https://www.gnu.org/licenses/agpl-3.0.html"

/** Public licensing page.
 *
 *  AGPL-3.0 §13 requires whoever runs this software over a network to offer
 *  every user the Corresponding Source of the version they are using. This
 *  page is that offer. The login screen links here instead of sending staff
 *  straight to a source-code host, and the guest booking footer links here
 *  for the same reason: the obligation applies to guests too.
 *
 *  The URL is configuration (`kamra_source_url` in site defaults), not a
 *  constant, so a self-hosted deployment can point at its own published fork.
 */
export default function Licensing() {
  const { t, lang } = useT()
  const [info, setInfo] = useState<SiteInfo | null>(null)
  const [langState, setLangState] = useState<Lang>(lang || getLang())

  useEffect(() => {
    setLangState(lang)
  }, [lang])

  useEffect(() => {
    getSiteInfo().then(setInfo).catch(() => setInfo({ demo_mode: false }))
  }, [])

  const version = info?.version
  const coreVersion = info?.core_version
  const sourceUrl = info?.source_url

  return (
    <div
      className="min-h-[100dvh] bg-[#f7f9fb] px-4 py-10"
      style={{ colorScheme: "light" }}
    >
      <div className="fixed inset-x-0 top-0 h-[5px] bg-[#1C3F38]" aria-hidden />
      <div className="mx-auto w-full max-w-2xl">
        <div className="mb-6 flex items-center justify-between gap-4">
          <Link to="/login" className="logo-chip" aria-label="ZIRI PMS">
            <img
              src={asset("ziri-logo.png")}
              alt="ZIRI PMS"
              className="h-14 w-auto"
            />
          </Link>
          <label className="flex items-center gap-2 text-xs text-[#6f7a71]">
            <span>{t("Language")}</span>
            <select
              className="rounded border border-[#E2E8F0] bg-[#ffffff] px-2 py-1 text-xs text-[#3f4941]"
              value={langState}
              onChange={(e) => {
                const next = e.target.value as Lang
                setLang(next)
                setLangState(next)
              }}
              aria-label={t("Language")}
            >
              {LANGS.map((l) => (
                <option key={l.code} value={l.code}>
                  {l.nativeLabel}
                </option>
              ))}
            </select>
          </label>
        </div>

        <article className="rounded border border-[#E2E8F0] bg-[#ffffff] p-6 sm:p-8">
          <p className="text-xs font-semibold uppercase tracking-[0.18em] text-[#1E7B4F]">
            {t("Licensing")}
          </p>
          <h1 className="mt-2 text-2xl font-semibold tracking-tight text-[#191c1e]">
            {t("Licensing & source code")}
          </h1>
          <p className="mt-3 text-sm leading-relaxed text-[#3f4941]">
            {t(
              "ZIRI PMS is free software, distributed under the GNU Affero General Public License version 3 (AGPL-3.0).",
            )}
          </p>

          {(version || coreVersion) && (
            <p className="mt-2 text-xs text-[#6f7a71]">
              {version && (
                <span>
                  {t("This deployment runs ZIRI PMS v{version}.", { version })}
                </span>
              )}
              {version && coreVersion && <span className="mx-1">·</span>}
              {coreVersion && (
                <span>{t("Kamra core {version}", { version: coreVersion })}</span>
              )}
            </p>
          )}

          <section className="mt-6 rounded border border-[#bbf7d0] bg-[#f0fdf4] p-4">
            <h2 className="text-sm font-semibold text-[#14532d]">
              {t("Corresponding Source")}
            </h2>
            <p className="mt-1 text-sm leading-relaxed text-[#3f4941]">
              {t(
                "The complete source code for the version running here is available at no charge at the link below.",
              )}
            </p>
            {sourceUrl ? (
              <a
                href={sourceUrl}
                target="_blank"
                rel="noreferrer"
                dir="ltr"
                className="mt-2 inline-block break-all text-sm font-medium text-[#1E7B4F] underline hover:text-[#00613a]"
              >
                {sourceUrl}
              </a>
            ) : (
              <p className="mt-2 text-sm text-[#6f7a71]">
                {t("The source offer is not configured on this site.")}
              </p>
            )}
          </section>

          <section className="mt-6 space-y-3 text-sm leading-relaxed text-[#3f4941]">
            <p>
              {t(
                "ZIRI PMS is a distribution of Kamra PMS, created by HeyKoala and contributors.",
              )}{" "}
              <a
                href={UPSTREAM_URL}
                target="_blank"
                rel="noreferrer"
                className="underline hover:text-[#1E7B4F]"
              >
                {t("Upstream project")}
              </a>
              .
            </p>
            <p>
              {t(
                "You may copy, modify and redistribute this software under the terms of the GNU AGPL-3.0. It comes with no warranty.",
              )}{" "}
              <a
                href={AGPL_URL}
                target="_blank"
                rel="noreferrer"
                className="underline hover:text-[#1E7B4F]"
              >
                {t("Read the full licence")}
              </a>
              .
            </p>
          </section>
        </article>

        <p className="mt-6 text-center text-xs text-[#6f7a71]">
          <Link
            to="/login"
            className="underline hover:text-[#1E7B4F]"
          >
            {t("Back to sign in")}
          </Link>
        </p>
      </div>
    </div>
  )
}
