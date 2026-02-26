import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';

const DEFAULT_SITE_URL = 'https://dev-docs.moodybeard.com';

function toDocPath(id: string): string {
	const normalized = id.replace(/^\/+|\/+$/g, '');
	return normalized ? `/${normalized}/` : '/';
}

function parsePubDate(value: unknown): Date | undefined {
	if (value instanceof Date && !Number.isNaN(value.getTime())) return value;
	if (typeof value !== 'string') return undefined;

	const parsed = new Date(value);
	return Number.isNaN(parsed.getTime()) ? undefined : parsed;
}

export async function GET(context: APIContext) {
	const docs = await getCollection('docs', ({ data }) => !data.draft);

	const items = docs
		.map((entry) => ({
			title: entry.data.title,
			description: entry.data.description,
			link: toDocPath(entry.id),
			pubDate: parsePubDate(entry.data.lastUpdated),
		}))
		.sort((a, b) => {
			const aTime = a.pubDate?.getTime() ?? 0;
			const bTime = b.pubDate?.getTime() ?? 0;
			if (aTime !== bTime) return bTime - aTime;
			return a.link.localeCompare(b.link, 'en');
		});

	return rss({
		title: 'dev-docs',
		description: 'dev-docs 문서 업데이트 RSS 피드',
		site: context.site ?? DEFAULT_SITE_URL,
		customData: '<language>ko-kr</language>',
		items,
	});
}
