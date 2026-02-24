import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';
import { readFileSync } from 'node:fs';
import { staticSidebar } from './src/config/sidebar.static.mjs';

function extractSectionKey(entry) {
	if (!entry || typeof entry !== 'object') return undefined;

	if (typeof entry.slug === 'string' && entry.slug) {
		return entry.slug.split('/')[0];
	}

	if (Array.isArray(entry.items)) {
		for (const child of entry.items) {
			const key = extractSectionKey(child);
			if (key) return key;
		}
	}

	return undefined;
}

function readGeneratedSidebarSections() {
	try {
		const raw = readFileSync(new URL('./src/config/sidebar.generated.json', import.meta.url), 'utf-8');
		const parsed = JSON.parse(raw);
		return Array.isArray(parsed) ? parsed : [];
	} catch {
		return [];
	}
}

function mergeSidebarWithGenerated(staticSidebar, generatedSidebar) {
	if (!Array.isArray(generatedSidebar) || generatedSidebar.length === 0) {
		return staticSidebar;
	}

	const merged = [...staticSidebar];

	for (const generatedSection of generatedSidebar) {
		const generatedKey = extractSectionKey(generatedSection);
		if (!generatedKey) {
			merged.push(generatedSection);
			continue;
		}

		const index = merged.findIndex((item) => extractSectionKey(item) === generatedKey);
		if (index === -1) merged.push(generatedSection);
		else merged[index] = generatedSection;
	}

	return merged;
}

const generatedSidebarSections = readGeneratedSidebarSections();

export default defineConfig({
	site: 'https://dev-docs.moodybeard.com',
	integrations: [
		starlight({
			title: 'dev-docs',
			components: {
				Head: './src/components/Head.astro',
				PageTitle: './src/components/PageTitle.astro',
				ContentPanel: './src/components/ContentPanel.astro',
			},
			head: [
				{
					tag: 'script',
					attrs: { type: 'application/ld+json' },
					content: JSON.stringify({
						'@context': 'https://schema.org',
						'@type': 'WebSite',
						name: 'dev-docs',
						url: 'https://dev-docs.moodybeard.com',
					}),
				},
			],
			locales: {
				root: { label: '한국어', lang: 'ko' },
				en: { label: 'English', lang: 'en' },
			},
			sidebar: mergeSidebarWithGenerated(staticSidebar, generatedSidebarSections),
			}),
			sitemap(),
		],
	});
