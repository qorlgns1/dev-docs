import { defineCollection } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

function preservePathCaseSlug({
	entry,
	base,
	data,
}: {
	entry: string;
	base: URL;
	data: Record<string, unknown>;
}) {
	if (typeof data.slug === 'string' && data.slug.trim()) {
		return data.slug.trim().replace(/^\/+|\/+$/g, '');
	}

	const entryUrl = new URL(encodeURI(entry), base);
	const relPath = path.relative(fileURLToPath(base), fileURLToPath(entryUrl)).split(path.sep).join('/');
	const ext = path.extname(relPath);
	const withoutExt = ext ? relPath.slice(0, -ext.length) : relPath;

	// Astro 기본 규칙과 동일하게 nested /index 만 제거하고 root index 는 유지한다.
	return withoutExt.replace(/\/index$/, '');
}

export const collections = {
	docs: defineCollection({
		loader: docsLoader({ generateId: preservePathCaseSlug }),
		schema: docsSchema(),
	}),
};
