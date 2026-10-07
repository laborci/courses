<script lang="ts">
  import { onMount, tick } from 'svelte';
  import { ProseMarkdown } from '@atom-forge/ui';
  let { html, dark = false }: { html: string; dark?: boolean } = $props();
  let container: HTMLDivElement;
  let mounted = $state(false);
  onMount(() => { mounted = true; });
  $effect(() => {
    const current = html;
    const theme = dark;
    if (!mounted) return;
    let cancelled = false;
    async function diagrams() {
      await tick();
      if (cancelled || !container) return;
      // Restore the source before rendering again after a theme or route change.
      container.innerHTML = current;
      const nodes = [...container.querySelectorAll<HTMLElement>('.mermaid-source')];
      if (!nodes.length) return;
      const { default: mermaid } = await import('mermaid');
      if (cancelled) return;
      mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: theme ? 'dark' : 'default', suppressErrorRendering: true });
      for (const [index, node] of nodes.entries()) {
        const source = node.textContent || '';
        try {
          const { svg } = await mermaid.render(`diagram-${Date.now()}-${index}`, source);
          if (cancelled) return;
          node.innerHTML = svg;
          node.classList.add('diagram');
        } catch {
          if (cancelled) return;
          node.textContent = source;
          node.classList.add('diagram-error');
          node.setAttribute('title', 'Invalid Mermaid diagram');
        }
      }
    }
    void diagrams();
    return () => { cancelled = true; };
  });
</script>
<ProseMarkdown>
  <div class="text-[15px] leading-[1.85] [&_h1]:text-[28px] [&_h1]:tracking-[-0.8px] min-[761px]:[&_h1]:text-[32px] [&_a]:text-accent [&_pre]:overflow-x-auto [&_pre]:rounded-[9px] [&_pre_code]:text-xs [&_img]:max-w-full [&_iframe.youtube]:my-7 [&_iframe.youtube]:aspect-video [&_iframe.youtube]:w-full [&_iframe.youtube]:rounded-[10px] [&_iframe.youtube]:border-0 [&_.mermaid-source]:whitespace-pre-wrap [&_.diagram]:flex [&_.diagram]:justify-center [&_.diagram]:bg-transparent [&_.diagram_svg]:h-auto [&_.diagram_svg]:max-w-full [&_.diagram-error]:border [&_.diagram-error]:border-error [&_.katex-display]:overflow-x-auto [&_.katex-display]:overflow-y-hidden [&_.katex-display]:p-2 [&_.callout]:my-6 [&_.callout]:rounded-[var(--radius-control)] [&_.callout]:border [&_.callout]:border-frame [&_.callout]:border-l-[3px] [&_.callout]:border-l-accent [&_.callout]:bg-surface [&_.callout]:text-canvas-contrast [&_.callout]:not-italic [&_.callout-title]:flex [&_.callout-title]:items-center [&_.callout-title]:gap-2.5 [&_.callout-title]:px-4 [&_.callout-title]:py-3 [&_.callout-title]:text-sm [&_.callout-title]:leading-normal [&_.callout-title]:font-semibold [&_.callout-icon]:m-0 [&_.callout-icon]:shrink-0 [&_.callout-icon]:text-accent [&_.callout-body]:px-4 [&_.callout-body]:pb-3.5 [&_.callout-body>:first-child]:mt-0 [&_.callout-body>:last-child]:mb-0 [&_details.callout>summary]:cursor-pointer [&_details.callout>summary]:list-none [&_details.callout>summary::-webkit-details-marker]:hidden [&_details.callout>summary]:after:ml-auto [&_details.callout>summary]:after:size-[7px] [&_details.callout>summary]:after:shrink-0 [&_details.callout>summary]:after:rotate-[-45deg] [&_details.callout>summary]:after:border-r-2 [&_details.callout>summary]:after:border-b-2 [&_details.callout>summary]:after:content-[''] [&_details.callout[open]>summary]:after:rotate-45 [&_.callout-title]:before:[quotes:none] [&_.callout-title]:after:[quotes:none] [&_.callout-body_p]:before:[quotes:none] [&_.callout-body_p]:after:[quotes:none]" bind:this={container}>{@html html}</div>
</ProseMarkdown>
