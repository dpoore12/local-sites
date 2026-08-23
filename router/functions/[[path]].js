// One Pages project serves every site. The hostname picks the folder.
export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const host = url.hostname.toLowerCase().replace(/^www\./, "");

  if (host.endsWith(".pages.dev") || host === "localhost") {
    return env.ASSETS.fetch(request);
  }

  const at = (path) => {
    const u = new URL(request.url);
    u.pathname = "/" + host + path;
    return env.ASSETS.fetch(new Request(u.toString(), request));
  };

  let res = await at(url.pathname);
  if (res.status === 404 && !url.pathname.endsWith("/")) {
    const retry = await at(url.pathname + "/");
    if (retry.status !== 404) return retry;
  }
  if (res.status === 404) {
    const home = await at("/");
    if (home.status === 200) {
      return new Response(home.body, { status: 404, headers: home.headers });
    }
  }
  return res;
}
